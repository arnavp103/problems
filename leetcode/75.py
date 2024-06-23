# 75 Sort Colors


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        from random import randint

        def quick_sort(nums: list[int], start: int, end: int) -> None:
            if start >= end:
                return

            pivot = randint(start, end)
            nums[start], nums[pivot] = nums[pivot], nums[start]

            left = start + 1
            right = end

            while left <= right:
                if nums[left] <= nums[start]:
                    left += 1
                elif nums[right] > nums[start]:
                    right -= 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

            nums[start], nums[right] = nums[right], nums[start]

            quick_sort(nums, start, right - 1)
            quick_sort(nums, right + 1, end)

        quick_sort(nums, 0, len(nums) - 1)
