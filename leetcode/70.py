# 70 Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/ - Easy


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # how many steps do you need with distance i
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2
        # with ways[3] dist = 3 so 1+1+1 or (1,2) or (2,1) so 3 ways
        # 4 = (1,1,1,1 or 1,1,2 or 1,2,1) - 1 to get to 3 or +2 (2,1,1 or 2,2)

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[-1]
