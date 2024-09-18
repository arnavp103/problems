# 191 Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits - Easy


class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 for c in bin(n)[2:] if c == "1")
