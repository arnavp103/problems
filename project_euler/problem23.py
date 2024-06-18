"""
A perfect number is a number for which the sum of its proper
divisors is exactly equal to the number.

For example, the sum of the proper divisors of 28 would
be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper
divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.

By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by
analysis even though it is known that the greatest number that
cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be
written as the sum of two abundant numbers.
"""


def solution() -> int:
    """return the sum of all positive integers which can't be written as the sum of two abundants"""

    def d(n: int) -> int:
        return sum(i for i in range(1, n) if n % i == 0)

    def is_abundant(n: int) -> bool:
        return d(n) > n

    limit = 28123
    # this is the bottleneck, but since the func runs in around 10 seconds idm
    abundant_numbers = {i for i in range(1, limit) if is_abundant(i)}

    # find the lower bound beyond which all integers can be the sum of two abundant numbers
    for top in range(limit, 0, -1):
        is_sum_of_abundant_numbers = False
        for abundant_number in abundant_numbers:
            if top - abundant_number in abundant_numbers:
                is_sum_of_abundant_numbers = True
                break
        # if you could write the number as the sum of two abundant numbers, then it's the top
        if is_sum_of_abundant_numbers:
            limit = top
        else:
            # otherwise you've found the number at which point
            # you can't write it as the sum of two abundant numbers
            break

    total = 0
    for i in range(1, limit):
        could_be_sum = False
        for abundant_number in abundant_numbers:
            if i - abundant_number in abundant_numbers:
                could_be_sum = True
                break
        if not could_be_sum:
            total += i

    return total


print(solution())

# 4179871 - correct
