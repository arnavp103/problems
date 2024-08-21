# 664 Strange Printer


class Solution:
    def strangePrinter(self, s: str) -> int:
        # this is a dp problem
        # we need to find the min number of operations to print the string
        # we can do this by finding the min number of operations to print the
        # substring s[i:j] and then subtracting 1 if s[i] == s[j]

        # we can store the computation for s[i:j] in a memo
        memo: dict[tuple[int, int], int] = {}

        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            # printing s[i:j] is at most printing s[i:j-1] + 1
            # may be less if s[i] == s[j]
            res = dp(i, j - 1) + 1

            for k in range(i, j):
                # if they're same char, try combining their prints
                # suppose s="aa" and i and j point to 0 and 1 index
                # so res = 2 (because s[i:(j-1)] = "a" and s[j] = "a")
                # then you have dp(s[i:i]) = 1 and dp(s[j:j-1]) = 0
                # so res gets set to 1
                if s[k] == s[j]:
                    sections = dp(i, k) + dp(k + 1, j - 1)
                    res = min(res, sections)

            memo[(i, j)] = res
            return res

        return dp(0, len(s) - 1)
