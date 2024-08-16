# 624 Maximum Distance in Arrays


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        smallest = 10**4
        second_smallest = 0
        smallest_ind = 0

        largest = -(10**4)
        second_largest = 0
        largest_ind = 0

        for i, arr in enumerate(arrays):
            if arr[0] < smallest:
                second_smallest = smallest
                smallest = arr[0]
                smallest_ind = i
            elif arr[0] < second_smallest:
                second_smallest = arr[0]

            # this needs to be >= so that they don't end up on the same spot
            if arr[-1] >= largest:
                second_largest = largest
                largest = arr[-1]
                largest_ind = i
            elif arr[-1] >= second_largest:
                second_largest = arr[-1]

        dist = largest - smallest

        if smallest_ind != largest_ind:
            return dist

        if largest - second_smallest >= second_largest - smallest:
            return largest - second_smallest

        return second_largest - smallest
