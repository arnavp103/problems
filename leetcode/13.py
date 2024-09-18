# 13 Roman to Integer
# https://leetcode.com/problems/roman-to-integer/ - Easy


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        prev = 0

        for c in s:
            curr = roman_map[c]

            if prev < curr:
                result += curr - 2 * prev
            else:
                result += curr

            prev = curr

        return result
