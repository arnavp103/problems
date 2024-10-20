# 670 Maximum Swap
# https://leetcode.com/problems/maximum-swap/ - Medium


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        last = {int(x): i for i, x in enumerate(num)}
        for i, x in enumerate(num):
            for d in range(9, int(x), -1):
                if d in last and last[d] > i:
                    num[i], num[last[d]] = num[last[d]], num[i]
                    return int(''.join(num))
        return int(''.join(num))
        