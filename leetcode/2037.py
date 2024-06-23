# 2037 Minimum Number of Moves to Seat Everyone


class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        moves = sum(abs(seat - student) for seat, student in zip(seats, students))
        return moves
