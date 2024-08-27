# 1325 Path with Maximum Probability
# https://leetcode.com/problems/path-with-maximum-probability/ - Medium

import heapq


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # this is just djiikstra's algorithm
        # with weighted edges and instead of adding the weights
        # we multiply them
        # we us a heap to get the largest probability

        graph = {}
        for i, (u, v) in enumerate(edges):
            if u not in graph:
                graph[u] = {}
            if v not in graph:
                graph[v] = {}
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]

        # this is a min heap
        # so we negate the probability
        # to get the maximum probability
        heap = [(-1, start_node)]
        visited = set()
        while heap:
            prob, node = heapq.heappop(heap)
            if node == end_node:
                return -prob
            if node in visited:
                continue
            visited.add(node)
            for neighbor, edge_prob in graph.get(node, {}).items():
                heapq.heappush(heap, (prob * edge_prob, neighbor))

        return 0.0
