# 409 Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/ - Easy

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        even_len = 0
        exist_odd = False

        for _, v in counts.items():
            even_len += 2 * (v // 2)
            if v % 2 != 0:
                exist_odd = True

        # one set of odd number of letters in the middle
        # remove the double counting from an odd
        return even_len + (1 if exist_odd else 0)
