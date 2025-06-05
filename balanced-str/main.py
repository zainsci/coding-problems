#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/check-balanced-string/
problem: https://leetcode.com/problems/check-balanced-string/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/check-balanced-string/submissions/1654105633/
"""


class Solution:
    # def isBalanced(self, num: str) -> bool:
    def isBalanced(self, num):
        return sum(int(x) for x in num[::2]) == sum(int(x) for x in num[1::2])


def main():
    sol = Solution()

    num = "1234"
    print(sol.isBalanced(num))

    num = "24123"
    print(sol.isBalanced(num))

    pass


if __name__ == "__main__":
    main()
