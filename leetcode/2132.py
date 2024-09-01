# 2132 Convert 1D Array Into 2D Array
# https://leetcode.com/problems/convert-1d-array-into-2d-array/ - Easy


class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != n * m:
            return []

        res = [[0] * n for _ in range(m)]

        for i, val in enumerate(original):
            res[i // n][i % n] = val

        return res
