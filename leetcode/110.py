# 110 Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/ - Easy

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def height(root, is_balanced) -> tuple[int, bool]:
            if root is None:
                return 0, True

            lh, lb = height(root.left, is_balanced)
            rh, rb = height(root.right, is_balanced)

            if abs(lh - rh) > 1:
                is_balanced = False

            return 1 + max(lh, rh), is_balanced and lb and rb

        _, bal = height(root, is_balanced)
        return bal
