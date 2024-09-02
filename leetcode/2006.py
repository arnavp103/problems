# 2006 Find the Student that Will Replace the Chalk
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/ - Medium


class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
        return 0
