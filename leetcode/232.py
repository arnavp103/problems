# 232 Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/ - Easy


class MyQueue:
    def __init__(self):
        self.recv = []
        self.out = []

    def push(self, x: int) -> None:
        self.recv.append(x)

    def pop(self) -> int:
        if len(self.out) == 0:
            while len(self.recv) > 0:
                el = self.recv.pop()
                self.out.append(el)

        return self.out.pop()

    def peek(self) -> int:
        if len(self.out) == 0:
            while len(self.recv) > 0:
                el = self.recv.pop()
                self.out.append(el)

        return self.out[-1]

    def empty(self) -> bool:
        if len(self.out) == 0:
            while len(self.recv) > 0:
                el = self.recv.pop()
                self.out.append(el)

        return len(self.out) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
