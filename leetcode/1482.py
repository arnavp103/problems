# 1482 Minimum Number of Days to Make m Bouquets


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def can_make_bouquets(days: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if can_make_bouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left
