# 264 Ugly Number II


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # you start with 0 2s, 0 3s, and 0 5s
        # the first ugly number is 1
        # then you have to keep adding the minimum of the previous ugly number

        ugly_numbers = [1]

        # keep an index of the last place
        # you incremented a 2, 3, or 5
        twos = 0
        threes = 0
        fives = 0

        for _ in range(1, n):
            prev = ugly_numbers[-1]

            if ugly_numbers[twos] * 2 <= prev:
                twos += 1

            if ugly_numbers[threes] * 3 <= prev:
                threes += 1

            if ugly_numbers[fives] * 5 <= prev:
                fives += 1

            mult_two = ugly_numbers[twos] * 2
            mult_three = ugly_numbers[threes] * 3
            mult_five = ugly_numbers[fives] * 5

            ugly_numbers.append(min(mult_two, mult_three, mult_five))

        print(ugly_numbers, len(ugly_numbers))
        return ugly_numbers[-1]
