# 3010 Divide an Array Into Subarrays With Minimum Cost I


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        cost = nums[0] # have to take the first element
        ordered = sorted(nums)
        bot_3 = ordered[:3]
        if cost in bot_3:
            return sum(bot_3)
        else:
            return cost + sum(bot_3[0:2])