# 2134 Minimum Swaps to Group All 1's Together II


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        num_ones = sum(1 for num in nums if num == 1)
        if num_ones == 0:
            return 0

        # move a sliding window of size num_ones counting the number of zeros
        min_zeros = sum(1 for num in nums[0:num_ones] if num == 0)

        num_zeros = min_zeros
        for ind, num in enumerate(nums):
            if ind < num_ones:
                continue
            if nums[ind - num_ones] == 0:
                num_zeros -= 1

            if num == 0:
                num_zeros += 1

            min_zeros = min(min_zeros, num_zeros)

        # now do all the circular wrap around cases
        for ind, num in enumerate(nums[0:num_ones]):
            if nums[(len(nums) + ind) - num_ones] == 0:
                num_zeros -= 1

            if num == 0:
                num_zeros += 1

            min_zeros = min(min_zeros, num_zeros)

        return min_zeros
