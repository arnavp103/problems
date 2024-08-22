# 1031 Maximum Sum of Two Non-Overlapping Subarrays


class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + num

        result = 0
        for i in range(len(nums) - firstLen + 1):
            for j in range(i + firstLen, len(nums) - secondLen + 1):
                result = max(
                    result,
                    prefix_sum[i + firstLen]
                    - prefix_sum[i]
                    + prefix_sum[j + secondLen]
                    - prefix_sum[j],
                )
            for j in range(i - secondLen + 1):
                result = max(
                    result,
                    prefix_sum[i + firstLen]
                    - prefix_sum[i]
                    + prefix_sum[j + secondLen]
                    - prefix_sum[j],
                )

        return result
