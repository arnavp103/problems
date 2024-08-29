# 984 Most Stones Removed with Same Row or Column
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/ - Medium


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        # like n queens problem

        rows = {}
        cols = {}
        for i, (x, y) in enumerate(stones):
            if x not in rows:
                rows[x] = []
            rows[x].append(i)
            if y not in cols:
                cols[y] = []
            cols[y].append(i)

        seen = set()

        def dfs(i):
            if i in seen:
                return 0
            seen.add(i)
            x, y = stones[i]
            count = 1
            for j in rows[x] + cols[y]:
                count += dfs(j)
            return count

        return sum(max(dfs(i) - 1, 0) for i in range(len(stones)))
