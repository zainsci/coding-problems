#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/transpose-matrix/
problem: https://leetcode.com/problems/transpose-matrix/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/transpose-matrix/submissions/1628396972/
"""


class Solution:
    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    def transpose(self, matrix):
        new_mat = [[None for _ in range(len(matrix))]
                   for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_mat[j][i] = matrix[i][j]

        return new_mat


def main():
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.transpose(matrix))

    matrix = [[1, 2, 3], [4, 5, 6]]
    print(sol.transpose(matrix))
    pass


if __name__ == "__main__":
    main()
