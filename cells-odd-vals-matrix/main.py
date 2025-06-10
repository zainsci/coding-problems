#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
problem: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/submissions/1659498297/
"""


class Solution:
    # def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
    def oddCells(self, m, n, indices):
        grid = [[0 for x in range(n)] for _ in range(m)]
        count = 0

        for idx in indices:
            r, c = idx

            for i in range(len(grid[r])):
                grid[r][i] += 1

                if grid[r][i] & 1:
                    count += 1
                else:
                    count -= 1

            for i in range(len(grid)):
                grid[i][c] += 1

                if grid[i][c] & 1:
                    count += 1
                else:
                    count -= 1

        return count


def main():
    sol = Solution()
    m = 2
    n = 3
    indices = [[0, 1], [1, 1]]
    print(sol.oddCells(m, n, indices))

    m = 2
    n = 2
    indices = [[1, 1], [0, 0]]
    print(sol.oddCells(m, n, indices))

    pass


if __name__ == "__main__":
    main()
