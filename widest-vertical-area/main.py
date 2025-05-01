#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
problem: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/submissions/1623055308/
"""


class Solution:
    # def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    def maxWidthOfVerticalArea(self, points):
        points = sorted([x for x, y in points])
        areas = []

        for i in range(len(points)-1):
            areas.append(abs(points[i]-points[i+1]))

        return max(areas)


def main():
    sol = Solution()

    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print(sol.maxWidthOfVerticalArea(points))

    points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    print(sol.maxWidthOfVerticalArea(points))

    pass


if __name__ == "__main__":
    main()
