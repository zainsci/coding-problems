#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/a-number-after-a-double-reversal/
problem: https://leetcode.com/problems/a-number-after-a-double-reversal/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/a-number-after-a-double-reversal/submissions/1652103610/
"""


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True

        return False if str(num)[-1] == "0" else True


def main():
    sol = Solution()

    num = 526
    print(sol.isSameAfterReversals(num))

    num = 1800
    print(sol.isSameAfterReversals(num))

    num = 0
    print(sol.isSameAfterReversals(num))

    pass


if __name__ == "__main__":
    main()
