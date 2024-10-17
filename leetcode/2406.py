# 2406 Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/ - Medium


class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        # algo inspired by line sweep algorithm from editorial
        point_height: dict[int, int] = {}
        for start, end in intervals:
            point_height[start] = point_height.get(start, 0) + 1
            point_height[end + 1] = point_height.get(end + 1, 0) - 1

        concurrent_intervals = 0
        max_concurrent_intervals = 0

        for point in sorted(point_height.keys()):
            concurrent_intervals += point_height[point]
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )

        return max_concurrent_intervals
