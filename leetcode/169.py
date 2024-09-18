# 169 Majority Element
# https://leetcode.com/problems/majority-element/ - Easy

from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_k = -1
        max_v = -1

        for k, v in counts.items():
            if v > max_v:
                max_k = k
                max_v = v

        return max_k
