# 135 Candy
# https://leetcode.com/problems/candy/ - Hard


class Solution:
    def candy(self, ratings: list[int]) -> int:
        given = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                given[i] = given[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                given[i] = max(given[i], given[i + 1] + 1)
        return sum(given)
