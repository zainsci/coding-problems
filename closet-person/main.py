#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-closest-person/
problem: https://leetcode.com/problems/find-closest-person/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-closest-person/submissions/1648673111/
"""


class Solution:
    # def findClosest(self, x: int, y: int, z: int) -> int:
    def findClosest(self, x, y, z):
        return 1 if abs(x - z) < abs(y - z) else 2 if abs(x - z) > abs(y - z) else 0


def main():
    sol = Solution()
    x = 2
    y = 7
    z = 4
    print(sol.findClosest(x, y, z))

    x = 2
    y = 5
    z = 6
    print(sol.findClosest(x, y, z))

    x = 1
    y = 5
    z = 3
    print(sol.findClosest(x, y, z))

    pass


if __name__ == "__main__":
    main()
