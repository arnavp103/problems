# 1 Two Sum


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}
        for i, num in enumerate(nums):
            if num in indices:
                indices[num].append(i)
            else:
                indices[num] = [i]

        for i, num in enumerate(nums):
            diff = target - num

            if diff in indices:
                for idx in indices[diff]:
                    if idx != i:
                        return [i, idx]
        return [-1]
