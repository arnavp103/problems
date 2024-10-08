# 179 Largest Number
# https://leetcode.com/problems/largest-number/ - Medium

import functools


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def bigger(a: int, b: int) -> int:
            fst = str(a)
            snd = str(b)

            fst_snd = int(fst + snd)
            snd_fst = int(snd + fst)

            return 1 if fst_snd > snd_fst else -1

        nums.sort(key=functools.cmp_to_key(bigger), reverse=True)

        return str(int("".join(str(num) for num in nums)))
