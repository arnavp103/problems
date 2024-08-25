# 226 Invert Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return None

            helper(root.left)
            helper(root.right)

            root.left, root.right = root.right, root.left
            return root

        return helper(root)
