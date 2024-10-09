# 1331 Rank Transform of an Array
# https://leetcode.com/problems/rank-transform-of-an-array/ - Easy

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if len(arr) == 0:
            return []

        indices = {}
        for i, num in enumerate(arr):
            if num in indices:
                indices[num].append(i)
                continue
            indices[num] = [i]

        asc = sorted(set(arr))
        ranks = {v: rank + 1 for rank, v in enumerate(asc)}
        return [ranks[num] for num in arr]