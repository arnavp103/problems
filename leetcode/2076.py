# 2076 Sum of Digits of String After Convert
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/ - Easy


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num = ""
        for char in s:
            num += str(ord(char) - ord("a") + 1)
        for _ in range(k):
            num = str(sum(int(digit) for digit in num))
        return int(num)
