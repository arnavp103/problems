# 1518 Water Bottles


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles + numBottles // numExchange
        leftover = numBottles % numExchange + numBottles // numExchange
        while leftover >= numExchange:
            total += leftover // numExchange
            leftover = leftover % numExchange + leftover // numExchange
        return total
