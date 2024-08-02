# 173 Binary Search Tree Iterator
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    i = 0

    def __init__(self, root: Optional[TreeNode]):
        ptr = root
        self.traversal = []

        stack = []
        while ptr or stack:
            while ptr:
                stack.append(ptr)
                ptr = ptr.left
            ptr = stack.pop()
            self.traversal.append(ptr.val)
            ptr = ptr.right

    def next(self) -> int:
        val = self.traversal[self.i]
        self.i += 1
        return val

    def hasNext(self) -> bool:
        return self.i < len(self.traversal)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
