# 35 Search Insert Position


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
