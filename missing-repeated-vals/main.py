#!/usr/bin/env python3
from collections import Counter, deque
from functools import reduce

"""
source: https://leetcode.com/problems/find-missing-and-repeated-values/
problem: https://leetcode.com/problems/find-missing-and-repeated-values/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-missing-and-repeated-values/submissions/1629305273/
"""


class Solution:
    # def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    def findMissingAndRepeatedValues(self, grid):
        grid = reduce(lambda x, y: x+y, grid)
        grid_sum = sum(grid)

        unique = set(grid)
        unique_sum = sum(unique)

        grid_len = len(grid)
        grid_len_sum = grid_len * (grid_len + 1) // 2

        missing = grid_len_sum - unique_sum
        repeated = grid_sum - unique_sum

        return [repeated, missing]


def main():
    sol = Solution()

    grid = [[1, 3], [2, 2]]
    print(sol.findMissingAndRepeatedValues(grid))

    grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
    print(sol.findMissingAndRepeatedValues(grid))

    pass


if __name__ == "__main__":
    main()
