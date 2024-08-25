# 733 Flood Fill
# https://leetcode.com/problems/flood-fill/ - Easy


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        stack = [(sr, sc)]
        starting_color = image[sr][sc]
        seen = set()

        def add_four_ways(row, col):
            if (
                row > 0
                and image[row - 1][col] == starting_color
                and (row - 1, col) not in seen
            ):
                stack.append((row - 1, col))
            if (
                row < len(image) - 1
                and image[row + 1][col] == starting_color
                and (row + 1, col) not in seen
            ):
                stack.append((row + 1, col))

            if (
                col > 0
                and image[row][col - 1] == starting_color
                and (row, col - 1) not in seen
            ):
                stack.append((row, col - 1))
            if (
                col < len(image[0]) - 1
                and image[row][col + 1] == starting_color
                and (row, col + 1) not in seen
            ):
                stack.append((row, col + 1))

        while len(stack) != 0:
            row, col = stack.pop()
            seen.add((row, col))
            image[row][col] = color
            add_four_ways(row, col)
        return image
