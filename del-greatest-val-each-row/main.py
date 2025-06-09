#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/delete-greatest-value-in-each-row/
problem: https://leetcode.com/problems/delete-greatest-value-in-each-row/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/delete-greatest-value-in-each-row/submissions/1658649632/
"""


class Solution:
    # def deleteGreatestValue(self, grid: List[List[int]]) -> int:
    def deleteGreatestValue(self, grid):
        count = 0
        grid = [sorted(row) for row in grid]

        for col in zip(*grid):
            count += max(col)

        return count


def main():
    sol = Solution()

    grid = [[1, 2, 4], [3, 3, 1]]
    print(sol.deleteGreatestValue(grid))

    grid = [[10]]
    print(sol.deleteGreatestValue(grid))

    pass


if __name__ == "__main__":
    main()
