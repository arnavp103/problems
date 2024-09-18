# 539 Minimum Time Difference
# https://leetcode.com/problems/minimum-time-difference/ - Medium


class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        time_vals: list[int] = sorted(
            int(time[:2]) * 60 + int(time[3:]) for time in timePoints
        )
        time_vals.append(time_vals[0] + 1440)
        return min(time_vals[i + 1] - time_vals[i] for i in range(len(time_vals) - 1))
