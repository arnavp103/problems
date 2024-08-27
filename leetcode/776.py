# 776 N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/ - Easy


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> list[int]:
        if not root:
            return []

        result = []
        for child in root.children:
            result.extend(self.postorder(child))

        result.append(root.val)
        return result
