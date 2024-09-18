# 14 Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/ - Easy


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        i = 0

        while True:
            letter = ""

            for w in strs:
                if i >= len(w):
                    return strs[0][:i]

                if letter == "":
                    letter = w[i]
                    continue

                if w[i] != letter:
                    return strs[0][:i]

            i += 1
