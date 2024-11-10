# 2641 Cousins in Binary Tree II

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to perform DFS and sum up the values at each depth.
        def dfs_sum_values(node, depth):
            if node is None:
                return
            # If we encounter a new depth, initialize sum for that depth.
            if len(depth_sums) <= depth:
                depth_sums.append(0)
            # Add the current node's value to the corresponding depth's sum.
            depth_sums[depth] += node.val
            # Recursive calls for the left and right subtrees, with increased depth.
            dfs_sum_values(node.left, depth + 1)
            dfs_sum_values(node.right, depth + 1)

        # Helper function to perform DFS and replace the values of non-root nodes.
        def dfs_replace_values(node, depth):
            if node is None:
                return
            # Calculate the combined value of the current node's children.
            children_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            # Replace the values of the left and right children.
            if node.left:
                node.left.val = depth_sums[depth] - children_sum
            if node.right:
                node.right.val = depth_sums[depth] - children_sum
            # Recursive calls for the left and right subtrees, with increased depth.
            dfs_replace_values(node.left, depth + 1)
            dfs_replace_values(node.right, depth + 1)

        # Initialize the list that will hold the sums of values at each depth.
        depth_sums = []
        # First DFS to calculate sums at each depth.
        dfs_sum_values(root, 0)
        # Set the root value to 0 since the question seems to be replacing non-root values.
        root.val = 0
        # Second DFS to replace values in the tree.
        dfs_replace_values(root, 1)
      
        return root
