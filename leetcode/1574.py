# 1574 Shortest Subarray to be Removed to Make Array Sorted
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/ - Medium

class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:

        if len(arr) == 1:
            return 0

        left = 0
        right = len(arr) - 1
        while left < len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1                
            if left == right:
                return 0
        
        while right > 1 and arr[right] >= arr[right - 1]:
            right -= 1
            if right == left:
                return 0

        min_len = min(len(arr) - left - 1, right)
        
        i = 0
        j = right
        while i <= left:
            while j < len(arr) and arr[j] < arr[i]:
                j += 1
           
            min_len = min(min_len, j - i - 1)
            i += 1

        return min_len
