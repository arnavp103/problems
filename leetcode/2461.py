# 2461 Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/ - Medium


from collections import Counter


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        # find max subarray sum with length k and all distinct
        # if less than k elements
        # return 0
        # sliding window

        freqs = Counter(nums[:k])
        curr_sum = sum(nums[:k])
        max_sum = 0

        if len(freqs) == k:
            max_sum = curr_sum

        for i in range(k, len(nums)):
            freqs[nums[i]] += 1
            freqs[nums[i - k]] -= 1
            if freqs[nums[i - k]] == 0:
                del freqs[nums[i - k]]

            curr_sum += nums[i]
            curr_sum -= nums[i - k]

            if len(freqs) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum
