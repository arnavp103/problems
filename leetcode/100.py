# 100 Same Tree
# https://leetcode.com/problems/same-tree/ - Easy

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if p is None or q is None:
                return p is None and q is None

            if p.val != q.val:
                return False

            return helper(p.left, q.left) and helper(p.right, q.right)

        return helper(p, q)
