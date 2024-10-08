# 1172 Dinner Plate Stacks
# https://leetcode.com/problems/dinner-plate-stacks/ - Hard

import bisect


class DinnerPlates:
    def __init__(self, capacity: int):
        self.last = 0
        self.cap = capacity
        self.stacks = [[]]
        self.free = []
        self.freeset = set()

    def push(self, val: int) -> None:
        for freespot in self.free:
            if freespot > self.last:
                break
            self.stacks[freespot].append(val)
            new_len = len(self.stacks[freespot])
            if new_len >= self.cap:
                self.freeset.remove(freespot)
                del self.free[bisect.bisect_left(self.free, freespot)]

            return

        len_last = len(self.stacks[self.last])
        if len_last >= self.cap:
            self.last += 1
            if len(self.stacks) <= self.last:
                self.stacks.append([])

        self.stacks[self.last].append(val)

    def pop(self) -> int:
        len_last = len(self.stacks[self.last])

        while len_last == 0 and self.last > 0:
            self.last -= 1
            len_last = len(self.stacks[self.last])

        if self.last == 0 and len_last == 0:
            return -1

        return self.stacks[self.last].pop()

    def popAtStack(self, index: int) -> int:
        if index > self.last:
            return -1

        stack_len = len(self.stacks[index])
        if stack_len == 0:
            return -1

        if index not in self.freeset:
            bisect.insort(self.free, index)
            self.freeset.add(index)

        return self.stacks[index].pop()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
