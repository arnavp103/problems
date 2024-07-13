# 2751 Robot Collisions
import heapq
from collections import deque


class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        # min heap of left wards robots
        # deque of right wards robots
        left_bots = []
        right_bots = []
        for i, (p, d) in enumerate(zip(positions, directions)):
            if d == "L":
                heapq.heappush(left_bots, (p, i))
            else:
                right_bots.append((p, i))

        right_bots.sort(key=lambda x: x[0])
        right_bots = deque(right_bots)

        while len(left_bots) > 0 and len(right_bots) > 0:
            left_pos, left_ind = heapq.heappop(left_bots)
            low_right_pos, low_right_ind = right_bots.popleft()

            while left_pos < low_right_pos:
                if len(left_bots) == 0:
                    # the right elements will stay till the end
                    return [h for h in healths if h > 0]
                left_pos, left_ind = heapq.heappop(left_bots)

            right_pos, right_ind = low_right_pos, low_right_ind
            can_skip = (abs(left_pos - right_pos)) == 1
            high_right_pos = -1

            # if the lp is bigger than the rp
            # see if we can get a closer match by decreasing the rp
            passed = []
            if not can_skip and len(right_bots) > 0:
                high_right_pos, high_right_ind = right_bots.pop()
                while left_pos < high_right_pos:
                    passed.append((high_right_pos, high_right_ind))
                    if len(right_bots) == 0:
                        for el in passed[::-1]:
                            right_bots.append(el)
                        break
                    high_right_pos, high_right_ind = right_bots.pop()

            if low_right_pos < high_right_pos < left_pos:
                right_bots.appendleft((low_right_pos, low_right_ind))
                for el in passed[::-1]:
                    right_bots.append(el)
                right_pos, right_ind = high_right_pos, high_right_ind

            left_health = healths[left_ind]
            right_health = healths[right_ind]

            if left_health == right_health:
                healths[left_ind] = 0
                healths[right_ind] = 0

            elif left_health < right_health:
                healths[left_ind] = 0
                healths[right_ind] -= 1
                right_bots.appendleft((right_pos, right_ind))
                right_bots = deque(sorted(right_bots, key=lambda x: x[0]))

            else:
                healths[left_ind] -= 1
                healths[right_ind] = 0
                heapq.heappush(left_bots, (left_pos, left_ind))

        return [h for h in healths if h > 0]
