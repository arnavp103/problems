# 2582 Pass the Pillow


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time >= 2 * (n - 1):
            time %= 2 * (n - 1)

        if n <= time <= 2 * n:
            return n - (time % n) - 1
        return time + 1


# do
