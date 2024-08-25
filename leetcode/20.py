# 20 Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if char == ")" and top != "(":
                    return False
                if char == "}" and top != "{":
                    return False
                if char == "]" and top != "[":
                    return False
        return len(stack) == 0
