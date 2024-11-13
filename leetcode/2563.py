# 2563 Count the Number of Fair Pairs
# https://leetcode.com/problems/count-the-number-of-fair-pairs/ - Medium


from bisect import bisect_left


class Solution:
    def count_fair_pairs(self, nums: list[int], lower: int, upper: int) -> int:
        # Sort the list of numbers to leverage binary search advantage.
        nums.sort()
        fair_pairs_count = 0

        # Iterate over each number to find suitable pairs.
        for index, num in enumerate(nums):
            # Find the left boundary for fair pairs.
            left_index = bisect_left(nums, lower - num, lo=index + 1)

            # Find the right boundary for fair pairs.
            right_index = bisect_left(nums, upper - num + 1, lo=index + 1)

            # Update the count of fair pairs by the number of elements that
            # fall between the calculated left and right boundaries.
            fair_pairs_count += right_index - left_index

        return fair_pairs_count
