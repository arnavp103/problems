# 1497. Check If Array Pairs Are Divisible by k
# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/ - Medium


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        modulos = [0] * k
        for num in arr:
            modulos[num % k] += 1
        
        if modulos[0] % 2 != 0:
            return False
        
        for i in range(1, k // 2 + 1):
            if modulos[i] != modulos[k - i]:
                return False
            
        return True