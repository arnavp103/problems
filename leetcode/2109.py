# 2109 Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/ - Medium

class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        result = ["" for _ in range(len(spaces) + len(s))]
        
        index = len(s) - 1
        space_index = len(spaces) - 1

        early = False
        for i in range(len(result) - 1, -1, -1):
            if early:
                early = False
                space_index -= 1
                result[i] = " "
                continue

            result[i] = s[index]

            if spaces[space_index] == index:
                early = True
            
            index -= 1

        print(result)
        return "".join(result)
        