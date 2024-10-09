# 150 Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/ - Medium


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-/*":
                b = stack.pop()
                a = stack.pop()
                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack.pop()
        