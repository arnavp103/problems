# 2053 Kth Distinct String in an Array

from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counts = Counter(arr)
        distincts = set()
        for key, v in counts.items():
            if v == 1:
                distincts.add(key)

        amnt = k
        for word in arr:
            if word in distincts:
                amnt -= 1
                if amnt == 0:
                    return word
        return ""
