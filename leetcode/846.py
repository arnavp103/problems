# 846 Hand of Straights


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        sorted_hand = sorted(hand)
        hands = []
        while len(sorted_hand):
            for i in range(groupSize):
                if len(sorted_hand) == 0:
                    return False

                if i == 0:
                    hands.append([sorted_hand.pop(0)])
                else:
                    for index, num in enumerate(sorted_hand):
                        if hands[-1][-1] + 1 == num:
                            hands[-1].append(num)
                            sorted_hand.pop(index)
                            break
                        elif sorted_hand[index] > hands[-1][-1] + 1:
                            return False
        return True
