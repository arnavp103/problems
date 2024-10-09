# 921 Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/ - Medium


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if c == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
        