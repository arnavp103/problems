# 3163 String Compression III
# https://leetcode.com/problems/string-compression-iii/ - Medium

class Solution:
    def compressedString(self, word: str) -> str:
        comp = "" # compressed string
        prev = word[0] # previous character
        length = 1

        for i in range(1, len(word)):
            if length == 9:
                comp += str(length) + prev
                prev = word[i]
                length = 1
                continue

            if word[i] == prev:
                length += 1
            else:
                comp += str(length) + prev
                prev = word[i]
                length = 1
        comp += str(length) + prev
        
        return comp