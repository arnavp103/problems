"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of 2^1000?
"""


def solution(n: int) -> int:
    """return the sum of the digits of 2^n"""
    return sum(int(digit) for digit in str(2**n))


print(solution(1000))

# 1366 - correct
