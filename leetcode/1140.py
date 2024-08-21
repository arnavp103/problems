# 1140 Stone Game II


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        # you have to take from the piles in order
        # looks like a simple recursive dp problem

        m = 1
        # stores the max num of stones you can get given an (i, m)
        # where i is the index of the piles you're on
        memo: dict[tuple[int, int], int] = {}

        # since we always assume that each player plays optimally
        # each entry in the memo should have the most stones you can get
        # that means when you subtract the opponents best play versus your
        # current play you can add the remaining stones because they are yours
        # otherwise they would be in your opponents best play
        prefix_sum = sum(piles)
        remaining = [prefix_sum]
        for pile in piles:
            prefix_sum -= pile
            remaining.append(prefix_sum)

        def dp(i, m):
            if i >= len(piles):
                return 0
            if (i, m) in memo:
                return memo[(i, m)]
            res = 0
            for x in range(1, min(2 * m, len(piles) - i) + 1):
                opp_best_play = dp(i + x, max(m, x))
                total = sum(piles[i : i + x])
                net = total - opp_best_play + remaining[i + x]
                if net > res:
                    res = net

            memo[(i, m)] = res
            return res

        result = dp(0, m)
        return result
