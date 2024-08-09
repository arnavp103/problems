# 840 Magic Squares In Grid


class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        # for a given index like (0, 2) which is the first row and the third column tells you the sum
        right = {}
        # same concept as right but for going down
        down = {}
        # going down right
        dr = {}
        # going down left
        dl = {}

        for row_ind, row in enumerate(grid):
            for col_ind, val in enumerate(row):
                if col_ind + 2 < len(row):
                    if (row_ind, col_ind) not in right:
                        right[(row_ind, col_ind)] = (
                            val + row[col_ind + 1] + row[col_ind + 2]
                        )
                if row_ind + 2 < len(grid):
                    if (row_ind, col_ind) not in down:
                        down[(row_ind, col_ind)] = (
                            val
                            + grid[row_ind + 1][col_ind]
                            + grid[row_ind + 2][col_ind]
                        )
                if row_ind + 2 < len(grid) and col_ind + 2 < len(row):
                    if (row_ind, col_ind) not in dr:
                        dr[(row_ind, col_ind)] = (
                            val
                            + grid[row_ind + 1][col_ind + 1]
                            + grid[row_ind + 2][col_ind + 2]
                        )
                if row_ind + 2 < len(grid) and col_ind - 2 >= 0:
                    if (row_ind, col_ind) not in dl:
                        dl[(row_ind, col_ind)] = (
                            val
                            + grid[row_ind + 1][col_ind - 1]
                            + grid[row_ind + 2][col_ind - 2]
                        )

        # iterate from the perspective of the top left
        count = 0
        for row_ind, row in enumerate(grid):
            for col_ind, val in enumerate(row):
                if col_ind + 2 < len(row) and row_ind + 2 < len(grid):
                    if right[(row_ind, col_ind)] == down[(row_ind, col_ind)] == down[
                        (row_ind, col_ind + 1)
                    ] == down[(row_ind, col_ind + 2)] == dr[(row_ind, col_ind)] == dl[
                        (row_ind, col_ind + 2)
                    ] and set(
                        [
                            row[col_ind],
                            row[col_ind + 1],
                            row[col_ind + 2],
                            grid[row_ind + 1][col_ind],
                            grid[row_ind + 1][col_ind + 1],
                            grid[row_ind + 1][col_ind + 2],
                            grid[row_ind + 2][col_ind],
                            grid[row_ind + 2][col_ind + 1],
                            grid[row_ind + 2][col_ind + 2],
                        ]
                    ) == set([1, 2, 3, 4, 5, 6, 7, 8, 9]):
                        count += 1
        return count
