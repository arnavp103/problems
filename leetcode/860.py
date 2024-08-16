# 860 Lemonade Change


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # always favor using the biggest bill for change as you possibly can
        fives = 0
        tens = 0
        for num in bills:
            if num == 5:
                fives += 1
            elif num == 10:
                tens += 1
                if fives > 0:
                    fives -= 1
                else:
                    return False
            elif num == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
