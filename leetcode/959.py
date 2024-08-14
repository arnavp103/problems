# 959 Regions Cut By Slashes


class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        roots = {}

        def find(x):
            if x not in roots:
                roots[x] = x
            while x != roots[x]:
                x = roots[x]
            return x

        def union(x, y):
            roots[find(x)] = find(y)

        # 0: top, 1: right, 2: bottom, 3: left
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell in "/ ":
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
                if cell in r"\ ":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if i > 0:
                    union((i, j, 0), (i - 1, j, 2))
                if j > 0:
                    union((i, j, 3), (i, j - 1, 1))
        return len(set(find(x) for x in roots))
