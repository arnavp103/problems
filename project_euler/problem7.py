"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.
What is the 10 001st prime number?
"""


def solution(n):
    """find the nth prime number"""
    size = 1
    primes = [2]
    num = 3
    while size < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
            size += 1
        num += 2

    return primes[-1]


print(solution(10001))

# 104743 - correct
