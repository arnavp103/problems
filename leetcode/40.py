# 40 Combination Sum II


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path, res):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                # skip an element if you've seen it
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(i + 1, target - candidates[i], path + [candidates[i]], res)

        res = []
        candidates.sort()
        backtrack(0, target, [], res)

        return res
