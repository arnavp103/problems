# 1568 Minimum Number of Days to Disconnect Island


class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        # you only need to check islands with 2 connections
        # anything less and the island count is guaranteed to remain the same

        def get_island_count():
            count = 0
            visited = set()

            for i in range(n):
                for j in range(m):
                    if grid[i][j] != 1 or (i, j) in visited:
                        continue

                    count += 1
                    stack = [(i, j)]
                    visited.add((i, j))

                    while stack:
                        x, y = stack.pop()
                        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                            nx, ny = x + dx, y + dy
                            if (
                                0 <= nx < n
                                and 0 <= ny < m
                                and grid[nx][ny] == 1
                                and (nx, ny) not in visited
                            ):
                                stack.append((nx, ny))
                                visited.add((nx, ny))

            return count

        n, m = len(grid), len(grid[0])

        if get_island_count() != 1:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if get_island_count() != 1:
                        return 1
                    grid[i][j] = 1

        return 2
