# 1438 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

import heapq


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        """
        heap with min max for each start
        """

        mins = []
        maxs = []
        max_len = 0

        start = 0

        for end, num in enumerate(nums):
            heapq.heappush(mins, (num, end))
            heapq.heappush(maxs, (-num, end))

            # if the diff between max and min is greater than limit
            # we need to move the start pointer
            while -maxs[0][0] - mins[0][0] > limit:
                # either move past the min or max
                start = min(maxs[0][1], mins[0][1]) + 1

                while mins[0][1] < start:
                    heapq.heappop(mins)
                while maxs[0][1] < start:
                    heapq.heappop(maxs)

            max_len = max(max_len, end - start + 1)

        return max_len
