# 906 Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/ - Medium


class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        unq_obstacles = set(tuple(obstacle) for obstacle in obstacles)
        x, y = 0, 0
        dx, dy = 0, 1
        max_distance = 0
        for command in commands:
            if command == -1:
                dx, dy = dy, -dx
            elif command == -2:
                dx, dy = -dy, dx
            else:
                for _ in range(command):
                    if (x + dx, y + dy) in unq_obstacles:
                        break
                    x, y = x + dx, y + dy
                    max_distance = max(max_distance, x**2 + y**2)
        return max_distance
