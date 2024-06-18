"""
Let d(n) be defined as the sum of proper divisors of n
 (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are:
1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110; therefore d(220) = 284.
The proper divisors of 284 are:
1, 2, 4, 71, and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def solution(n: int) -> int:
    """return the sum of all amicable numbers under n"""

    def d(n: int) -> int:
        return sum(i for i in range(1, n) if n % i == 0)

    amicable_numbers = set()
    for a in range(1, n):
        b = d(a)
        if a != b and d(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)

    return sum(amicable_numbers)


print(solution(10000))

# 31626 - correct
