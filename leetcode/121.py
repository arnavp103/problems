# 121 Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = float("inf")
        max_profit = 0

        for n in prices:
            if n < lowest:
                lowest = n

            if n - lowest > max_profit:
                max_profit = n - lowest

        return max_profit
