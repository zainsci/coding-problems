#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/determine-color-of-a-chessboard-square/
problem: https://leetcode.com/problems/determine-color-of-a-chessboard-square/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/determine-color-of-a-chessboard-square/submissions/1656024845/
"""


class Solution:
    # def squareIsWhite(self, coordinates: str) -> bool:
    def squareIsWhite(self, coordinates):
        return (ord(coordinates[0])-96 + int(coordinates[1])) % 2 != 0


def main():
    sol = Solution()

    coordinates = "a1"
    print(sol.squareIsWhite(coordinates))

    coordinates = "h3"
    print(sol.squareIsWhite(coordinates))

    coordinates = "c7"
    print(sol.squareIsWhite(coordinates))

    pass


if __name__ == "__main__":
    main()
