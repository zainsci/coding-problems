#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-asterisks/
problem: https://leetcode.com/problems/count-asterisks/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-asterisks/submissions/1636321199/
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([s.split("|")[x].count("*")
                    for x in range(0, len(s.split("|")), 2)])


def main():
    sol = Solution()

    s = "l|*e*et|c**o|*de|"
    print(sol.countAsterisks(s))

    s = "iamprogrammer"
    print(sol.countAsterisks(s))

    pass


if __name__ == "__main__":
    main()
