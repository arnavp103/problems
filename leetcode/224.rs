// 224 Basic Calculator
use std::iter::Peekable;
use std::vec::IntoIter;

#[derive(Debug)]
enum Token {
    Number(i32),
    Plus,
    Minus,
    LeftParen,
    RightParen,
}

#[derive(Debug)]
enum AST {
    Number(i32),
    Add(Box<AST>, Box<AST>),
    Subtract(Box<AST>, Box<AST>),
    Negate(Box<AST>),
}

struct Solution;

impl Solution {
    fn tokenize(s: String) -> Vec<Token> {
        let mut tokens = Vec::new();
        let mut chars = s.chars().peekable();
        while let Some(c) = chars.next() {
            match c {
                '0'..='9' => {
                    let mut num = c.to_digit(10).unwrap() as i32;
                    while let Some('0'..='9') = chars.peek() {
                        num = num * 10 + chars.next().unwrap().to_digit(10).unwrap() as i32;
                    }
                    tokens.push(Token::Number(num));
                }
                '+' => tokens.push(Token::Plus),
                '-' => tokens.push(Token::Minus),
                '(' => tokens.push(Token::LeftParen),
                ')' => tokens.push(Token::RightParen),
                ' ' => (),
                _ => panic!("Invalid character"),
            }
        }
        tokens
    }

    fn parse_term(tokens: &mut Peekable<IntoIter<Token>>) -> AST {
        let next = tokens.next();
        match next {
            Some(Token::Number(n)) => AST::Number(n),
            Some(Token::LeftParen) => {
                let expr = Solution::parse_expression(tokens);
                match tokens.next() {
                    Some(Token::RightParen) => (),
                    _ => panic!("Expected right paren"),
                }
                expr
            }
            Some(Token::Minus) => {
                let expr = Solution::parse_term(tokens);
                AST::Negate(Box::new(expr))
            }
            _ => panic!("Invalid token"),
        }
    }

    fn parse_expression(tokens: &mut Peekable<IntoIter<Token>>) -> AST {
        let mut lhs = Solution::parse_term(tokens);

        // make sure the parser is left associative by peeking
        while let Some(&Token::Plus) | Some(&Token::Minus) = tokens.peek() {
            let op = tokens.next().unwrap();
            let rhs = Solution::parse_term(tokens);
            // keep adding to the lhs
            match op {
                Token::Plus => lhs = AST::Add(Box::new(lhs), Box::new(rhs)),
                Token::Minus => lhs = AST::Subtract(Box::new(lhs), Box::new(rhs)),
                _ => panic!("Invalid token"),
            }
        }
        lhs
    }

    pub fn parse(tokens: Vec<Token>) -> AST {
        let mut tokens = tokens.into_iter().peekable();
        // since there's only one top level expression, we can just call parse_expression
        Solution::parse_expression(&mut tokens)
    }

    fn eval(ast: AST) -> i32 {
        match ast {
            AST::Number(n) => n,
            AST::Add(lhs, rhs) => Solution::eval(*lhs) + Solution::eval(*rhs),
            AST::Subtract(lhs, rhs) => Solution::eval(*lhs) - Solution::eval(*rhs),
            AST::Negate(expr) => -Solution::eval(*expr),
        }
    }

    pub fn calculate(s: String) -> i32 {
        let tokens = Solution::tokenize(s);
        let ast = Solution::parse(tokens);
        Solution::eval(ast)
    }
}

fn main() {
    let c = "2 - 1 + 2";
    let tokens = Solution::tokenize(c.to_string());
    let ast = Solution::parse(tokens);
    println!("{:?}", ast);

    let res = Solution::calculate(c.to_string());
    println!("{}", res); // 3 correct
}
