# 1248 Count Number of Nice Subarrays


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        quick index based solution
        """

        odd_indices = [i for i, num in enumerate(nums) if num % 2 == 1]
        if len(odd_indices) < k:
            return 0

        count = 0

        for start_ind, start in enumerate(odd_indices):
            end = start_ind + k - 1
            if end >= len(odd_indices):
                break

            left = start - (odd_indices[start_ind - 1] if start_ind > 0 else -1)
            right = (
                odd_indices[end + 1] if end + 1 < len(odd_indices) else len(nums)
            ) - odd_indices[end]

            count += left * right

        return count
