# 1346 Check If N and Its Double Exist
# https://leetcode.com/problems/check-if-n-and-its-double-exist/ - Easy


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False
