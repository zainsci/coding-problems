#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-the-pivot-integer/
problem: https://leetcode.com/problems/find-the-pivot-integer/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-the-pivot-integer/submissions/1628887082/
"""


class Solution:
    # def pivotInteger(self, n: int) -> int:
    def pivotInteger(self, n):
        if n == 1:
            return n

        left = sum([x for x in range(1, n+1)])
        last = rigt = n

        while last > 0:

            if left == rigt:
                return last

            left -= last
            rigt += last-1
            last -= 1

        return -1


def main():
    sol = Solution()

    n = 8
    print(sol.pivotInteger(n))

    n = 1
    print(sol.pivotInteger(n))

    n = 4
    print(sol.pivotInteger(n))
    pass


if __name__ == "__main__":
    main()
