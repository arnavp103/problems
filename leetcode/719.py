# # 719 Find K-th Smallest Pair Distance


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        # i came up with the first two solutions of the editorial independently
        # and apparently the second solution wouldn't have even timed out on a non interpreted language
        # but i ultimately had to read the editorial and do the binary search + dp solution

        nums.sort()
        max_el = nums[-1]
        max_diff = max_el * 2

        prefix_count = [0] * max_diff
        # a frequency table basically
        value_count = [0] * (max_el + 1)

        index = 0
        for dist in range(max_diff):
            # finds all the numbers that are less than or equal to dist
            while index < len(nums) and nums[index] <= dist:
                index += 1
            prefix_count[dist] = index

        for i, _ in enumerate(nums):
            value_count[nums[i]] += 1

        # get the number of pairs
        def count_pairs(max_dist):
            count = 0
            index = 0
            while index < len(nums):
                val = nums[index]
                amnt = value_count[val]

                pairs_with_larger_diffs = (
                    prefix_count[min(val + max_dist, len(prefix_count) - 1)]
                    - prefix_count[val]
                )

                pairs_with_same_diffs = amnt * (amnt - 1) // 2

                count += pairs_with_larger_diffs * amnt + pairs_with_same_diffs

                while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                    index += 1
                index += 1

            return count

        left, right = 0, max_el
        while left < right:
            mid = (left + right) // 2
            count = count_pairs(mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left
