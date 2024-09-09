# 2411 Spiral Matrix IV
# https://leetcode.com/problems/spiral-matrix-iv/ - Medium

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> list[list[int]]:
        matrix = [[-1] * n for _ in range(m)]

        row, col = 0, 0
        dr, dc = 0, 1

        while head:
            matrix[row][col] = head.val
            head = head.next

            if not (
                0 <= row + dr < m
                and 0 <= col + dc < n
                and matrix[row + dr][col + dc] == -1
            ):
                dr, dc = dc, -dr

            row += dr
            col += dc

        return matrix
