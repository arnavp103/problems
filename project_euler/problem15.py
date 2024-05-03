"""
Starting in the top left corner of a 2×2 grid, and only
being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import comb

# each path must have n right moves and n down moves
# so the total number of moves is 2n
# we must choose n of these moves to be right/down moves

# you can think of arranging all the moves in a sequence
# mmmmmmmm  (8 moves for a 4x4 grid)
# mddmdmmd (randomly choose 4 to be down moves)
# rddrdrrd (then the rest must be right moves)


def solution(n: int) -> int:
    """return the number of paths through an n x n grid"""
    return comb(2 * n, n)


print(solution(20))

# 137846528820 - correct
