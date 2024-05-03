"""
The sum of all the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def solution(n: int) -> int:
    """find the sum of all primes below n"""
    # representing the numbers from 0 to n-1 as a list of booleans
    primes = [True] * n

    primes[0], primes[1] = False, False
    for i in range(2, n):
        # if i is prime, all multiples of i are not prime
        if primes[i]:
            for j in range(i**2, n, i):
                primes[j] = False

    return sum(i for i in range(n) if primes[i])


print(solution(2_000_000))

# 142913828922 - correct
