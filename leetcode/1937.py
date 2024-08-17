# 1937 Maximum Number of Points with Cost


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        # had to read the editorial but didn't read the code
        # need to work on my dynamic programming

        left_max = [0] * len(points[0])
        right_max = [0] * len(points[0])
        curr_row = points[0]

        for i, _ in enumerate(curr_row):
            if i > 0:
                left_max[i] = max(left_max[i - 1] - 1, curr_row[i])
            else:
                left_max[i] = curr_row[i]

        for i in range(len(curr_row) - 1, -1, -1):
            if i < len(curr_row) - 1:
                right_max[i] = max(right_max[i + 1] - 1, curr_row[i])
            else:
                right_max[i] = curr_row[i]

        for row in points[1:]:
            for i, _ in enumerate(row):
                curr_row[i] = row[i] + max(left_max[i], right_max[i])
                if i > 0:
                    left_max[i] = max(left_max[i - 1] - 1, curr_row[i])
                else:
                    left_max[i] = curr_row[i]

            for i in range(len(row) - 1, -1, -1):
                if i < len(row) - 1:
                    right_max[i] = max(right_max[i + 1] - 1, curr_row[i])
                else:
                    right_max[i] = curr_row[i]

        return max(curr_row)
