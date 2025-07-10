#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
problem: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/submissions/1693531453/
"""


class Solution:
    # def removeTrailingZeros(self, num: str) -> str:
    def removeTrailingZeros(self, num):
        return str(int(num[::-1]))[::-1]


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
