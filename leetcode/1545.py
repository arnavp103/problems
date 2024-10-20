# 1545 Find Kth Bit in Nth Binary String

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cache: dict[int, str] = {1: "0"}

        def invert(bitstring: str) -> str:
            return "".join(["0" if c == "1" else "1" for c in bitstring])

        def helper(n: int) -> str:
            if n in cache: 
                return cache[n]
            
            cache[n] = helper(n-1) + "1" + invert(helper(n-1))[::-1]
            return cache[n]
        
        return helper(n)[k-1]