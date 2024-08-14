# 703 Kth Largest Element in a Stream

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap: list[int] = []
        heapq.heapify(self.heap)
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            # if the newly added element is smaller
            # then it gets popped
            # otherwise it's either the remaining heap[0] is the kth largest
            heapq.heappop(self.heap)
        return self.heap[0]
