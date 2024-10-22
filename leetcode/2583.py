# 2583 Kth Largest Sum in a Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = [0] 
        max_level = 0

        def level_sum(root: Optional[TreeNode], curr: int) -> None:
            if curr > max_level:
                level_sums.append(0)
            if root is None:
                return
            
            level_sums[curr] += root.val
            level_sum(root.left, curr + 1)
            level_sum(root.right, curr + 1)
            return 
        
        level_sum(root, 0)

        # swap k to zero based indexing
        k -= 1

        level_sums.sort(reverse=True)
        return -1 if level_sums[k] == 0 else level_sums[k]
    