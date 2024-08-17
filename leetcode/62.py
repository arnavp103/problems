# 62 Unique Paths

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # this is similar to that project euler problem
        # basically we have m-1 Downs and n-1 Rights to distribute
        # because we have to reach [m-1][n-1]

        # so for example m = 3, n = 2
        # all combinations of 2 Ds and 1 R
        # "DDR", "DRD", "RDD"
        # same thing as having 3 slots
        # and choosing where 2 of the Ds go
        # the Rs naturally fall into the remaining slots

        return math.comb(m + n - 2, n - 1)
