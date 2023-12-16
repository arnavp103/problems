// 412 FizzBuzz

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut answer = vec![];
        for i in 1..=n {
            if (i % 3 == 0 && i % 5 == 0) {
                answer.push(String::from("FizzBuzz"));
            } else if (i % 5 == 0) {
                answer.push(String::from("Buzz"));
            } else if (i % 3 == 0) {
                answer.push(String::from("Fizz"));
            } else {
                answer.push(i.to_string());
            }
        }
        answer
    }
}
