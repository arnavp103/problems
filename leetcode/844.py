# 844 Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/ - Easy


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        buf1 = ["" for _ in s]
        buf2 = ["" for _ in t]

        i1 = 0
        i2 = 0

        for char in s:
            if char == "#":
                i1 = max(i1 - 1, 0)
                buf1[i1] = ""
                continue
            buf1[i1] = char
            i1 += 1

        for char in t:
            if char == "#":
                i2 = max(i2 - 1, 0)
                buf2[i2] = ""
                continue
            buf2[i2] = char
            i2 += 1
            continue

        s1 = "".join(buf1)
        s2 = "".join(buf2)

        return s1 == s2
