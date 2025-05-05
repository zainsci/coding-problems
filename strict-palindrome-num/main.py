#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/strictly-palindromic-number/
problem: https://leetcode.com/problems/strictly-palindromic-number/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/strictly-palindromic-number/submissions/1626501443/
"""


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n >= 4:
            return False


def main():
    sol = Solution()

    n = 9
    print(sol.isStrictlyPalindromic(n))

    n = 4
    print(sol.isStrictlyPalindromic(n))

    pass


if __name__ == "__main__":
    main()
