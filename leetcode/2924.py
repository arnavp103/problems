# 2924 Find Champion II
# https://leetcode.com/problems/find-champion-ii/ - Medium


class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # basically asking for starting node with topo sort
        # else return -1

        # build graph
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # find starting node
        start = []
        for i in range(n):
            if indegree[i] == 0:
                start.append(i)

        # if no starting node
        if not start:
            return -1

        # if multiple starting node
        if len(start) > 1:
            return -1

        # topo sort
        res = []
        while start:
            u = start.pop()
            res.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    start.append(v)

        # if not all node visited
        if len(res) != n:
            return -1

        return res[0]
