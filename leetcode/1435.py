# 1435 XOR Queries of a Subarray
# https://leetcode.com/problems/xor-queries-of-a-subarray/ - Medium

class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        ans = [0 for _ in queries]
        cache = {}

        def xor_range(l, r) -> int:
            res = arr[l]
            t = l + 1

            if l in cache:
                # index of the best value
                # we can use from cache
                max_less_r = -1

                for v in cache[l].keys():
                    if v > r:
                        continue
                    max_less_r = max(max_less_r, v)

                if max_less_r != -1:
                    t = max_less_r + 1
                    res = cache[l][t-1]

            while t <= r:
                res ^= arr[t]
                t += 1

            if l not in cache:
                cache[l] = {}

            # inclusive l, r
            cache[l][r] = ans
            return res


        for i, (l, r) in enumerate(queries):
            ans[i] = xor_range(l,r)

        return ans
