"""
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2, the first terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum of the even-valued terms.
"""


def solution():
    """solve the problem"""
    total = 0
    a = 1
    b = 2
    while b < 4000000:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    return total


print(solution())

# 4613732 - correct
