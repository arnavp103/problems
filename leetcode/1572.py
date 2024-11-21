# 1572 Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/ - Easy


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        diagonal_sum = 0

        for i in range(n):
            diagonal_sum += mat[i][i]
            diagonal_sum += mat[i][n - i - 1]

        if n % 2 == 1:
            # Subtract the middle element if the matrix has an odd number of rows and columns.
            diagonal_sum -= mat[n // 2][n // 2]

        return diagonal_sum
