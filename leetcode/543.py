# 543 Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/ - Easy

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root) -> tuple[int, int]:
            if root is None:
                return (0, 0)

            left_rm, left_lp = helper(root.left)
            right_rm, right_rp = helper(root.right)

            my_m = max(left_rm, right_rm) + 1
            my_p = left_rm + 1 + right_rm

            big_p = max(my_p, left_lp, right_rp)

            return (my_m, big_p)

        return max(helper(root)) - 1
