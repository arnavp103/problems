# 2696 Minimum String Length After Removing Substrings


class Solution:
    def minLength(self, s: str) -> int:
        stack: list[str] = []
        for char in s:
            if char == "B" and stack and stack[-1] == "A":
                stack.pop()
            elif char == "D" and stack and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
