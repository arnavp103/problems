# 235 Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ - Medium


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # constraint: all node.val are unique

        res = None

        def helper(root, found_p, found_q):
            nonlocal res
            if root is None:
                return False, False

            fpl, fql = helper(root.left, found_p, found_q)
            fpr, fqr = helper(root.right, found_p, found_q)

            fp = (root == p) or fpl or fpr
            fq = (root == q) or fql or fqr

            if fp and fq and res is None:
                res = root

            return fp, fq

        helper(root, False, False)
        return res  # type: ignore
