#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sort-the-students-by-their-kth-score/
problem: https://leetcode.com/problems/sort-the-students-by-their-kth-score/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/sort-the-students-by-their-kth-score/submissions/1626937230/
"""


class Solution:
    # def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
    def sortTheStudents(self, score, k):
        levels = {}

        for arr in score:
            levels[arr[k]] = arr

        sort = sorted(levels.keys())[::-1]

        ans = []
        for i in range(len(sort)):
            ans.append(levels[sort[i]])

        return ans


def main():
    sol = Solution()

    score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
    k = 2
    print(sol.sortTheStudents(score, k))

    score = [[3, 4], [5, 6]]
    k = 0
    print(sol.sortTheStudents(score, k))

    pass


if __name__ == "__main__":
    main()
