# 3133 Minimum Array End
# https://leetcode.com/problems/minimum-array-end/ - Medium

class Solution:
    def minEnd(self, n: int, x: int) -> int:        
        n -= 1
        ans = x
        
        # had to look this up unfortunately
        for i in range(31):
            if x >> i & 1 ^ 1:
                ans |= (n & 1) << i
                n >>= 1
        ans |= n << 31
        return ans