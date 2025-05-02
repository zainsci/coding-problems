#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-center-of-star-graph/
problem: https://leetcode.com/problems/find-center-of-star-graph/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-center-of-star-graph/submissions/1623933071/
"""


class Solution:
    # def findCenter(self, edges: List[List[int]]) -> int:
    def findCenter(self, edges):
        # SOLUTION: COURTESY OF NOOR
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]


def main():
    sol = Solution()

    edges = [[1, 2], [2, 3], [4, 2]]
    print(sol.findCenter(edges))

    edges = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(sol.findCenter(edges))

    pass


if __name__ == "__main__":
    main()
