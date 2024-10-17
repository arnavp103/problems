# 1963 Minimum Number of Swaps to Make the String Balanced


class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        swaps = 0
        for char in s:
            if char == "[":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                swaps += 1
                # why balance = 1?
                # you can always swap in such a way that
                # the balance is 1 swapping a pair of brackets such that both of them make a balanced pair
                balance = 1
        return swaps
