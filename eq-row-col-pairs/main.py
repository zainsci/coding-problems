#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/equal-row-and-column-pairs/
problem: https://leetcode.com/problems/equal-row-and-column-pairs/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/equal-row-and-column-pairs/submissions/1651833609/
"""


class Solution:
    # def equalPairs(self, grid: List[List[int]]) -> int:
    def equalPairs(self, grid):
        count = 0
        cols = []
        for j in range(len(grid)):
            col = [grid[k][j] for k in range(len(grid))]
            cols.append(col)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i] == cols[j]:
                    count += 1

        return count


def main():
    sol = Solution()

    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    print(sol.equalPairs(grid))

    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    print(sol.equalPairs(grid))

    pass


if __name__ == "__main__":
    main()
