import collections


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        lucky_numbers = [num for num, freq in count.items() if num == freq]
        return max(lucky_numbers) if lucky_numbers else -1
