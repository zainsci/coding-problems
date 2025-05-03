#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
problem: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/submissions/1624710857/
"""


class Solution:
    # def minimumSum(self, num: int) -> int:
    def minimumSum(self, num):
        digs = sorted([int(d) for d in str(num)])
        n = len(digs)
        total = 0

        for i in range(n // 2):
            left = digs[i]
            right = digs[n-1-i]
            combo = left * 10 + right
            total += combo

        return total


def main():
    sol = Solution()

    num = 2932
    print(sol.minimumSum(num))

    num = 4009
    print(sol.minimumSum(num))

    pass


if __name__ == "__main__":
    main()
