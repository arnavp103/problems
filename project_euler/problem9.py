"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solution(n: int) -> int:
    """find the product of the Pythagorean triplet for which a + b + c = n"""
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return 0


print(solution(1000))

# 31875000 - correct
