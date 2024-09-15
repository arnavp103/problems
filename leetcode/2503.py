# 2503 Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/ - Medium

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_val = max(nums)
        longest = 0
        i = 0
        while i < len(nums):
            if nums[i] != max_val:
                i += 1
                continue

            length = 1
            i += 1
            while i < len(nums):
                if nums[i] != max_val:
                    break
                i += 1
                length += 1

            longest = max(longest, length)

        return longest
