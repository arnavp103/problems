# 1508 Range Sum of Sorted Subarray Sums


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        arr = [nums[0]]
        # table for dp to quickly generate arr
        table = []
        # first index is the start index
        # second index is the end index (inclusive)
        # table[1][4] is the sum from nums[1:5]
        # table[0][2] is the sum from nums[0:3]

        for i in range(0, n):
            if i == 0:
                table.append(nums.copy())
                for j in range(1, n):
                    table[0][j] += table[0][j - 1]
                    arr.append(table[0][j])
                continue

            table.append([0] * n)
            for k in range(i, n):
                res = table[0][k] - table[0][k - 1] + table[1][k - 1]
                table[1][k] = res
                arr.append(res)
            table.pop(0)

        arr.sort()

        return sum(num for num in arr[left - 1 : right]) % (10**9 + 7)
