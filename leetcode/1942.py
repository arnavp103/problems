# 1942 The Number of the Smallest Unoccupied Chair
# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/ - Medium
from heapq import heappush, heappop
from bisect import bisect_left


class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        target = times[targetFriend][0]
        times.sort()
        heap: list[tuple[int, int]] = []
        chairs = list(range(len(times)))
        chairs.sort()
        for _i, (start, end) in enumerate(times):
            while heap and heap[0][0] <= start:
                _, chair = heappop(heap)
                chairs.insert(bisect_left(chairs, chair), chair)
            chair = chairs.pop(0)
            if start == target:
                return chair
            heappush(heap, (end, chair))
        return -1
