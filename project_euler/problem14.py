"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Which starting number, under one million, produces the longest chain?
"""


def collatz(n: int) -> int:
    """return the length of the collatz sequence starting at n"""
    length = 1
    while n != 1:
        length += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return length


def solution(limit: int) -> int:
    """return the starting number under limit that produces the longest collatz sequence"""
    return max(range(1, limit), key=collatz)


print(solution(1_000_000))

# 837799 - correct
