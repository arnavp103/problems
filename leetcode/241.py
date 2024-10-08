# 241 Different Ways to Add Parentheses
# https://leetcode.com/problems/different-ways-to-add-parentheses/ - Medium

import itertools


class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def compute(a, b, op):
            if op == "+":
                return a + b

            if op == "-":
                return a - b

            return a * b

        def dfs(expression):
            if expression.isdigit():
                return [int(expression)]

            result = []
            for i, c in enumerate(expression):
                if c in "+-*":
                    left = dfs(expression[:i])
                    right = dfs(expression[i + 1 :])
                    for lft, rht in itertools.product(left, right):
                        result.append(compute(lft, rht, c))

            return result

        return dfs(expression)
