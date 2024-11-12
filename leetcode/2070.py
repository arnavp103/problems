# 2179 Most Beautiful Item for Each Query
# https://leetcode.com/problems/most-beautiful-item-for-each-query/ - Medium


class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        # items[i] = [price_i, beauty_i]
        # sort items by price
        items.sort(key=lambda x: x[0])

        # then we make it sorted by beauty by removing elements with higher price but lower beauty
        fixed_items = []
        prev_beauty = -1
        for price, beauty in items:
            if beauty > prev_beauty:
                fixed_items.append((price, beauty))
                prev_beauty = beauty

        # now for each query we just binary search for the last item with price <= query
        def binary_search(query, items):
            left, right = 0, len(items)
            while left < right:
                mid = (left + right) // 2
                if items[mid][0] <= query:
                    left = mid + 1
                else:
                    right = mid
            return items[left - 1][1] if left > 0 else 0

        answers = []
        for query in queries:
            answers.append(binary_search(query, fixed_items))

        return answers
