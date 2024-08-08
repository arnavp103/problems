# 885 Spiral Matrix III


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> list[list[int]]:
        # go one right one down, then two left two up, then three right three down, etc.
        direction = "r"
        step_size = 1

        pos = [rStart, cStart]
        visited = [[rStart, cStart]]

        def add_if_valid(pos):
            r, c = pos
            if 0 <= r < rows and 0 <= c < cols:
                visited.append([r, c])

        while len(visited) < rows * cols:
            if direction == "r":
                for _ in range(step_size):
                    pos[1] += 1
                    add_if_valid(pos)
                direction = "d"
            elif direction == "d":
                for _ in range(step_size):
                    pos[0] += 1
                    add_if_valid(pos)
                step_size += 1
                direction = "l"
            elif direction == "l":
                for _ in range(step_size):
                    pos[1] -= 1
                    add_if_valid(pos)
                direction = "u"
            elif direction == "u":
                for _ in range(step_size):
                    pos[0] -= 1
                    add_if_valid(pos)
                step_size += 1
                direction = "r"

        return visited
