# 632 Smallest Range Covering Elements from K Lists
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/ - Hard

from heapq import heappush, heappop


class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap: list[tuple[int, int, int]] = []
        max_val = float("-inf")
        for i, num in enumerate(nums):
            heappush(heap, (num[0], i, 0))
            max_val = max(max_val, num[0])
        min_range = float("inf")
        result = [0, 0]
        while len(heap) == len(nums):
            val, i, j = heappop(heap)
            if max_val - val < min_range:
                min_range = max_val - val
                result = [val, int(max_val)]
            if j + 1 < len(nums[i]):
                heappush(heap, (nums[i][j + 1], i, j + 1))
                max_val = max(max_val, nums[i][j + 1])
        return result
