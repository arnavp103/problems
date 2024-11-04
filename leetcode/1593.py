# 1593 Split a String Into the Max Number of Unique Substrings


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(start: int, seen: set[str]) -> int:
            if start == len(s):
                return 0

            result = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring in seen:
                    continue

                seen.add(substring)
                result = max(result, 1 + dfs(end, seen))
                seen.remove(substring)

            return result

        return dfs(0, set())