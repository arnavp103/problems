# 3553 Check if Two Chessboard Squares Have the Same Color
# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/ - Easy


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # convert the letters to numbers
        # a1 -> 11
        # f3 -> 63
        # h5 -> 85
        c1 = ord(coordinate1[0]) - ord("a") + 1
        c2 = int(coordinate1[1])
        # if both nums are same parity, then black
        # same parity means sum is even
        black1 = (c1 + c2) % 2 == 0

        o1 = ord(coordinate2[0]) - ord("a") + 1
        o2 = int(coordinate2[1])
        black2 = (o1 + o2) % 2 == 0
        return black1 == black2
