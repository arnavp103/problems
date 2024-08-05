# 1460 Make Two Arrays Equal by Reversing Subarrays

from collections import Counter


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)
