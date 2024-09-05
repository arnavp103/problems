# 2155 Find Missing Observations
# https://leetcode.com/problems/find-missing-observations/ - Medium


class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        total_sum = mean * (n + len(rolls))
        remaining_sum = total_sum - sum(rolls)
        if remaining_sum < n or remaining_sum > 6 * n:
            return []

        missing_rolls = []
        for i in range(n):
            if i == n - 1:
                missing_rolls.append(remaining_sum)
            else:
                missing_rolls.append(1)
                remaining_sum -= 1

        # back distribute the remaining sum if > 6
        # you have to start from the second last
        bp = len(missing_rolls) - 2
        while bp >= 0 and missing_rolls[-1] > 6:
            missing_rolls[bp] += 5
            missing_rolls[-1] -= 5
            bp -= 1

        return missing_rolls
