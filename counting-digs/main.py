#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-the-digits-that-divide-a-number/
problem: https://leetcode.com/problems/count-the-digits-that-divide-a-number/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-the-digits-that-divide-a-number/submissions/1625584339/
"""


class Solution:
    def countDigits(self, num: int) -> int:
        digs = list(str(num))
        ans = 0
        for dig in digs:
            if num % int(dig) == 0:
                ans += 1

        return ans


def main():
    sol = Solution()

    num = 7
    print(sol.countDigits(num))

    num = 121
    print(sol.countDigits(num))

    num = 1248
    print(sol.countDigits(num))

    pass


if __name__ == "__main__":
    main()
