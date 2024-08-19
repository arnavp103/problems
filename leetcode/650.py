# 650 2 Keys Keyboard


class Solution:
    def minSteps(self, n: int) -> int:
        amount = 1
        steps = 0
        buffer = 0

        while amount < n:
            if n % amount == 0:
                buffer = amount
                steps += 1

            amount += buffer
            steps += 1

        return steps


"""
          2 46
6 -> 5 : cpcpp

          23 69
9 -> 6 : cppcpp

           23 69 12    2 4 8 12
12 -> 7 : cppcpp p    cpcpcp p

           23 6
15 -> 8 : cppcpppp   cppppcpp

x < y

x * y involves y pastes

y * x involves x pastes

so obv y * x is preferred

but to get y * x we need to get from x -> y

y * x is better than x * y by (y-x) pastes
but to get from x -> y we need (y-x) pastes as long as buffer = 1

what if buffer is not 1

let's say we're going to 60 = 2 * 30, 12 * 5 (more relevant)
eventually one of the factors is always going to be prime
that's the last one we can commit to so we can maintain this invariant
because to move from one prime to another coprime factor we need buffer = 1
"""
