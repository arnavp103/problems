# 3011 Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/ - Medium

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # can only swap two adjacent elements if have same number of set bits
        bits = [bin(num).count('1') for num in nums]
        iter = 0
        while iter < len(nums):
            for i in range(len(nums) - 1):
                if bits[i] == bits[i + 1] and nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    bits[i], bits[i + 1] = bits[i + 1], bits[i]
            iter += 1
        return sorted(nums) == nums
    