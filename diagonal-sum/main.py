#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/matrix-diagonal-sum/
problem: https://leetcode.com/problems/matrix-diagonal-sum/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/matrix-diagonal-sum/submissions/1629617348/
"""


class Solution:
    # def diagonalSum(self, mat: List[List[int]]) -> int:
    def diagonalSum(self, mat):
        left = 0
        right = len(mat)-1
        count = []

        while left < len(mat):

            if left == right:
                count.append(mat[left][left])
            else:
                count.append(mat[left][left])
                count.append(mat[left][right])

            left += 1
            right -= 1

        return sum(count)


def main():
    sol = Solution()
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print(sol.diagonalSum(mat))

    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    print(sol.diagonalSum(mat))

    mat = [[5]]
    print(sol.diagonalSum(mat))

    mat = [[7, 3, 1, 9],
           [3, 4, 6, 9],
           [6, 9, 6, 6],
           [9, 5, 8, 5]]
    print(sol.diagonalSum(mat))

    pass


if __name__ == "__main__":
    main()
