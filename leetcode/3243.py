# 3243 Shortest Distance After Road Addition Queries I
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/ - Medium


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        # let's do this the simple way with
        # bfs and adjusting the adjlist after each query

        adjlist = [[i + 1] for i in range(n - 1)]

        # get the distance from 0 to n-1
        def djikstra(adjlist: list[list[int]]) -> int:
            import queue

            pq = queue.PriorityQueue()
            pq.put((0, 0))
            visited = set()
            while not pq.empty():
                distance, node = pq.get()
                if node == n - 1:
                    return distance
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in adjlist[node]:
                    if neighbor not in visited:
                        pq.put((distance + 1, neighbor))

            return -1

        # get the initial distance
        initial_distance = djikstra(adjlist)
        print(initial_distance)

        ans = []

        for query in queries:
            adjlist[query[0]].append(query[1])
            ans.append(djikstra(adjlist))

        return ans
