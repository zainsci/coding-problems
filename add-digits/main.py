#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/add-digits/
problem: https://leetcode.com/problems/add-digits/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/add-digits/submissions/1650143974/
"""


class Solution:
    # def addDigits(self, num: int) -> int:
    def addDigits(self, num):
        while num >= 10:
            num = sum(int(x) for x in str(num))
        return num


# one-liner
# class Solution:
#     # def addDigits(self, num: int) -> int:
#     def addDigits(self, num):
#         return 0 if num == 0 else 1 + (num - 1) % 9


def main():
    sol = Solution()

    num = 38
    print(sol.addDigits(num))

    num = 0
    print(sol.addDigits(num))

    pass


if __name__ == "__main__":
    main()
