# 1861 Rotating the Box - Medium
# https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2024-11-23


class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        # since we there's no horizontal movement
        # we can work on each row independently

        def transpose_row(row: list[str]) -> list[list[str]]:
            col = [[] for _ in row]
            bottom = len(col) - 1  # if we see a stone, it should go to current bottom

            # loop over the row in reverse
            # keep track of the floor height
            for i in range(len(row) - 1, -1, -1):
                if row[i] == "#":
                    col[bottom].append("#")
                    bottom -= 1
                elif row[i] == "*":
                    col[i].append("*")
                    bottom = i - 1

            # fill the rest with empty spaces
            for i in range(len(col)):
                if len(col[i]) == 0:
                    col[i].append(".")

            return col

        transposed = [transpose_row(row) for row in box]

        m = len(box)
        n = len(box[0])
        ans = []

        for i in range(n):
            new_row = []
            for j in range(m - 1, -1, -1):
                new_row.append(transposed[j][i][0])

            ans.append(new_row)

        return ans
