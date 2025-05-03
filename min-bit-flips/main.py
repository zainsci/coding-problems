#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
problem: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/submissions/1624676342/
"""


class Solution:
    # def minBitFlips(self, start: int, goal: int) -> int:
    def minBitFlips(self, start, goal):
        start_str = str(bin(start)).replace("0b", "")
        goal_str = str(bin(goal)).replace("0b", "")

        long = max(len(start_str), len(goal_str))
        start_str = ("0"*(long-len(start_str)))+start_str
        goal_str = ("0"*(long-len(goal_str)))+goal_str

        count = 0
        for i in range(len(start_str)):
            if start_str[i] != goal_str[i]:
                count += 1

        return count


def main():
    sol = Solution()

    start = 10
    goal = 7
    print(sol.minBitFlips(start, goal))

    start = 3
    goal = 4
    print(sol.minBitFlips(start, goal))

    start = 81
    goal = 87
    print(sol.minBitFlips(start, goal))

    pass


if __name__ == "__main__":
    main()
