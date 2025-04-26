#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
problem: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/submissions/1618763983/
"""


class Solution:
    # def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    def minMovesToSeat(self, seats, students):
        seats = sorted(seats)
        students = sorted(students)
        moves = []

        for i in range(len(seats)):
            moves.append(abs(seats[i]-students[i]))

        return sum(moves)


def main():
    sol = Solution()

    seats = [3, 1, 5]
    students = [2, 7, 4]
    print(sol.minMovesToSeat(seats, students))

    seats = [4, 1, 5, 9]
    students = [1, 3, 2, 6]
    print(sol.minMovesToSeat(seats, students))

    seats = [2, 2, 6, 6]
    students = [1, 3, 2, 6]
    print(sol.minMovesToSeat(seats, students))


if __name__ == "__main__":
    main()
