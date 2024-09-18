# 136 Single Number
# https://leetcode.com/problems/single-number/ - Easy


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans: set[int] = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
                continue
            if n not in ans:
                ans.add(n)

        return list(ans)[0]
