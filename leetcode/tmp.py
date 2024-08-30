# 2803 Modify Graph Edge Weights
# https://leetcode.com/problems/modify-graph-edge-weights/ - Hard

import heapq


class Solution:
    def modifiedGraphEdges(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        destination: int,
        target: int,
    ) -> list[list[int]]:
        # obv djikstras
        # try iterating through all negative edges and changing the weight to 1
        # because if our solution is less than target, we can always
        # add the difference onto one of the edges

        # since the max value of a negative edge is 1e9, if we do have
        # a shortest path that reaches target, then set everything else to 2e9
        top = int(2e9)
        graph = [[] for _ in range(n)]
        for n1, n2, w in edges:
            # cannot take negative edges
            if w == -1:
                continue
            graph[n1].append((n2, w))
            graph[n2].append((n1, w))

        def djikstra(source, destination) -> int:
            min_dist = [top] * n
            min_dist[source] = 0
            heap = [(0, source)]

            while heap:
                dist, node = heapq.heappop(heap)

                if dist > min_dist[node]:
                    continue

                neighbors = graph[node]
                for neighbor, edge_weight in neighbors:
                    # if the shortest distance to the node is already
                    # greater than the target, we can't reach the destination
                    # in target weight
                    total_dist = dist + edge_weight
                    if total_dist > target or total_dist > min_dist[neighbor]:
                        continue
                    min_dist[neighbor] = total_dist

                    heapq.heappush(heap, (total_dist, neighbor))

            # if we cant go from src to dest
            # because of -1 edges, then we can fix those
            # so make sure returned val > target
            return min_dist[destination]

        curr_shortest = djikstra(source, destination)

        # can only make the path shorter, not longer
        if curr_shortest < target:
            return []

        reached_target = curr_shortest == target

        for edge in edges:
            if edge[2] == -1:
                # if reached target, set all other -1 edges to 2e9
                if reached_target:
                    edge[2] = top
                    # dont need to change the graph
                    # because we'll never call djikstras again

                # otherwise we might be able to make a shorter path
                else:
                    edge[2] = 1
                    graph[edge[0]][edge[1]] = 1
                    graph[edge[1]][edge[0]] = 1

            if not reached_target:
                new_shortest = djikstra(source, destination)
                # if smaller we can just set it to the difference
                if new_shortest <= target:
                    reached_target = True
                    edge[2] += target - new_shortest
                    # dont need to change the graph
                    # because we'll never call djikstras again

        return edges if reached_target else []
