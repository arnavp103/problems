"""
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solution(n: int) -> int:
    """find the lcm of numbers from 1 to 20"""

    def gcd(a: int, b: int) -> int:
        """euclid's algorithm to find gcd of two numbers"""
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(a: int, b: int) -> int:
        """find the lcm of two numbers"""
        return a * b // gcd(a, b)

    lcm_num = 1
    for i in range(1, n + 1):
        lcm_num = lcm(lcm_num, i)
    return lcm_num


print(solution(20))

# 232792560 - correct
