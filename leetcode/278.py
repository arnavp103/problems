# 278 First Bad Version
# https://leetcode.com/problems/first-bad-version/ - Easy


# The isBadVersion API is already defined for you.
def _isBadVersion(version: int) -> bool:
    """assumed to be working as a black box"""
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
