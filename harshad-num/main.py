#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/harshad-number/
problem: https://leetcode.com/problems/harshad-number/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/harshad-number/submissions/1637442321/
"""


class Solution:
    # def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        return sum([int(i) for i in str(x)]) if x % sum([int(i) for i in str(x)]) == 0 else -1


def main():
    sol = Solution()

    x = 18
    print(sol.sumOfTheDigitsOfHarshadNumber(x))

    x = 23
    print(sol.sumOfTheDigitsOfHarshadNumber(x))

    pass


if __name__ == "__main__":
    main()
