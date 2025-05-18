#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-odd-binary-number/
problem: https://leetcode.com/problems/maximum-odd-binary-number/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-odd-binary-number/submissions/1637482902/
"""


class Solution:
    # def maximumOddBinaryNumber(self, s: str) -> str:
    def maximumOddBinaryNumber(self, s):
        os = s.count("1")
        zs = s.count("0")

        return "1"*(os-1) + "0"*zs + "1"


def main():
    sol = Solution()

    s = "010"
    print(sol.maximumOddBinaryNumber(s))

    s = "0101"
    print(sol.maximumOddBinaryNumber(s))

    pass


if __name__ == "__main__":
    main()
