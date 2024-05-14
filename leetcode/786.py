# 786 K-th Smallest Prime Fraction

from fractions import Fraction


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        fracs = []
        for num in arr:
            for den in arr:
                if num < den:
                    fracs.append(Fraction(num, den))
        # fracs.sort() # too slow

        kth_frac = self.kth_order_statistic(fracs, k)
        return [kth_frac.numerator, kth_frac.denominator]

    def kth_order_statistic(self, arr: list[Fraction], k: int) -> Fraction:
        if len(arr) == 1:
            return arr[0]
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        if k <= len(left):
            return self.kth_order_statistic(left, k)
        elif k == len(left) + 1:
            return pivot
        else:
            return self.kth_order_statistic(right, k - len(left) - 1)
