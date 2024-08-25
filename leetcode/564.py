# 564 Find the Closest Palindrome


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)

        candidates = set()
        candidates.add("9" * (length - 1))
        candidates.add("1" + "0" * (length - 1) + "1")
        prefix = int(n[: (length + 1) // 2])
        for i in [-1, 0, 1]:
            prefix_str = str(prefix + i)
            if length % 2 == 0:
                candidates.add(prefix_str + prefix_str[::-1])
            else:
                candidates.add(prefix_str + prefix_str[:-1][::-1])
        candidates.discard(n)
        candidates = sorted(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        return candidates[0]
