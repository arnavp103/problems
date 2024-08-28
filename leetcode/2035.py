# 2035 Count Sub Islands
# https://leetcode.com/problems/count-sub-islands/ - Medium


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        sub_islands = 0

        def dfs(i, j):
            if (
                i < 0
                or i >= len(grid2)
                or j < 0
                or j >= len(grid2[0])
                or grid2[i][j] == 0
            ):
                return True

            grid2[i][j] = 0
            # first check if its in grid1
            res = grid1[i][j]
            res &= dfs(i + 1, j)
            res &= dfs(i - 1, j)
            res &= dfs(i, j + 1)
            res &= dfs(i, j - 1)
            return res

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    sub_islands += dfs(i, j)

        return sub_islands
