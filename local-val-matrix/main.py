#! /bin/python3


"""
source: https://leetcode.com/problems/largest-local-values-in-a-matrix/
problem: https://leetcode.com/problems/largest-local-values-in-a-matrix/
type: easy
site: LeetCode
submission: https://leetcode.com/problems/largest-local-values-in-a-matrix/submissions/1592068826/
"""


class Solution:
    # def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
    def largestLocal(self, grid):
        maxLocal = [[] for x in range(len(grid)-2)]

        for i in range(len(grid[0])-2):
            for j in range(len(grid[0])-2):
                x1, y1, z1 = grid[i][j], grid[i][j+1], grid[i][j+2]
                x2, y2, z2 = grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2]
                x3, y3, z3 = grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]

                maxLocal[i].append(max([x1, x2, x3, y1, y2, y3, z1, z2, z3]))

        return maxLocal


def main():
    grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    sol = Solution()
    res = sol.largestLocal(grid)
    print(res)

    grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
        1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    res = sol.largestLocal(grid)
    print(res)

    return


if __name__ == "__main__":
    main()
