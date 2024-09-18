# 104 Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/ - Easy

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0
            return 1 + max(helper(root.left), helper(root.right))

        return helper(root)
