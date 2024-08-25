# 145 Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/ - Easy

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def helper(root: Optional[TreeNode]) -> None:
            if root is None:
                return

            helper(root.left)
            helper(root.right)

            res.append(root.val)

        helper(root)
        return res
