# 338 Counting Bits
# https://leetcode.com/problems/counting-bits/ - Easy


class Solution:
    def countBits(self, n: int) -> list[int]:
        return [sum(1 for c in bin(x)[2:] if c == "1") for x in range(n + 1)]
