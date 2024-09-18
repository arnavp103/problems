# 67 Add Binary
# https://leetcode.com/problems/add-binary/ - Easy


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a, base=2)
        b_num = int(b, base=2)

        res = a_num + b_num

        return bin(res)[2:]
