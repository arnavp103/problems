# 1405 Longest Happy String
# https://leetcode.com/problems/longest-happy-string/ - Medium

from heapq import heappush, heappop


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result: list[str] = []

        # start with the most frequent character
        heap: list[tuple[int, str]] = []
        if a:
            heappush(heap, (-a, "a"))
        if b:
            heappush(heap, (-b, "b"))
        if c:
            heappush(heap, (-c, "c"))

        while heap:
            freq, char = heappop(heap)
            freq = -freq
            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break
                freq2, char2 = heappop(heap)
                freq2 = -freq2
                result.append(char2)
                freq2 -= 1
                if freq2:
                    heappush(heap, (-freq2, char2))
                heappush(heap, (-freq, char))
            else:
                result.append(char)
                freq -= 1
                if freq:
                    heappush(heap, (-freq, char))

        return "".join(result)
