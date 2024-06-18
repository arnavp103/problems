"""
n! means n × (n - 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def solution(n: int) -> int:
    """return the sum of the digits of n!"""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return sum(int(digit) for digit in str(factorial))


print(solution(100))

# 648 - correct
