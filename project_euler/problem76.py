"""
It is possible to write five as a sum in exactly six different ways:

                4 + 1
                3 + 2
                3 + 1 + 1
                2 + 2 + 1
                2 + 1 + 1 + 1
                1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

ANALYSIS = """
This seems like a dynamic programming problem. Basically
We have a tree of possible sums starting with n 1s and then n-1 1s and 1 2, and
at each step we can combine the sums in different ways.

The tree is not necessarily binary.
For example we can represent 7 as 3 + 2 + 1 + 1. From that sum, in one
step we can either get:

    3 + 2 + 2
    3 + 3 + 1
    4 + 2 + 1

Nodes in the tree will also crossover and share children.
We could get to 4 + 2 + 1 from 3 + 2 + 1 + 1 or 4 + 1 + 1 + 1.

## attempt 1:

This suggests a top down memoization approach. The cache will store the number of children of a node.

We start with n 1s. We have a method that generates all possible options in one step. We then recurse on those options since the cache will start unavailable.

We fill in the cache with sum of all possible children of our term. In the end
we just read off the number of nodes in the DAG.

### result: this failed precisely because the nodes crossover. there could be two intermediate nodes that look at their children and see that there are 2 ways to get to n but they actually have the same child which ends up being double counted

## attempt 2:

Some research reveals that this question is asking for the partition
of a positive integer. You can think of n as a set that's getting split into subsets which are the expressions.

Let's try splitting the problem even further into subproblems.

We can try to solve the case for n provided we have (n-1) and
we have a limit of how many terms can be used in the expression.

So for example
n = 7, k = 2
    6 + 1
    5 + 2
    4 + 3


n = 6, k = 2
    5 + 1
    4 + 2
    3 + 3

n = 4, k = 3
    2 + 1 + 1

Can get the sum of all the k's for each n using the simpler k's first.

Let's try and do k = 3 for n = 7.

    5 + 1 + 1
    4 + 2 + 1
    3 + 3 + 1
    --------- <- these three are just (n-1, k-1) with a 1 added to them

    3 + 2 + 2 <- apparently this is just (n-k, k)

    Let's try using this to do a bottom up solution.

"""


def generate_children(term: list[int]) -> list[tuple[int, ...]]:
    """return all possible children of a term"""
    children: set[tuple[int, ...]] = set()

    term = sorted(term, reverse=True)

    for i in range(len(term) - 1):
        child = term.copy()
        child[i] += child[i + 1]
        child.pop(i + 1)

        new_child = tuple(sorted(child))
        if new_child == tuple(term):
            continue
        children.add(new_child)

    return list(children)


def solution(n: int) -> int:
    """return the number of ways n can be written as a sum of at least two positive integers"""

    # the base case is just n itself
    cache = {(n,): 0}
    # a tuple of n 1s
    root = (1,) * n

    cache_hits = 0
    iterations = 0

    def ways(term: tuple[int, ...]) -> int:
        nonlocal cache_hits, iterations
        iterations += 1
        print(f"iteration{iterations}: {term}")

        if term in cache:
            print(f"cache hit: {term}")
            cache_hits += 1
            return cache[term]  # type: ignore

        children = generate_children(list(term))
        total = 1 + sum(ways(child) for child in children)
        cache[term] = total  # type: ignore
        return total

    sol = ways(root)
    print(f"hit rate: {(cache_hits / iterations) * 100}% out of {iterations}")
    print(cache)

    return sol


# print(solution(5)) - wrong


def solution2(n: int) -> int:
    """return the number of ways n can be written as at least two positive integers by attempt 2"""

    # rows = k represent the number of terms in the expression
    # so k = 1 means we're looking at expressions with 1 term which is just n
    # cols = n represent the number we're trying to split

    # we keep a zero term and zero col to play nice with indices
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        table[1][i] = 1  # only one way to split n into 1 term

    for k in range(1, n + 1):
        for result in range(1, n + 1):
            if k > result:
                table[k][result] = 0
                continue
            if k == result:
                table[k][result] = 1
                continue

            table[k][result] = table[k - 1][result - 1] + table[k][result - k]

    return sum(table[i][n] for i in range(1, n))


print(solution2(100))

# 190569291 - correct
