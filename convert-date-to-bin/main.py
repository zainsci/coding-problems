#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/convert-date-to-binary/
problem: https://leetcode.com/problems/convert-date-to-binary/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/convert-date-to-binary/submissions/1635425389/
"""


class Solution:
    # def convertDateToBinary(self, date: str) -> str:
    def convertDateToBinary(self, date):
        return "-".join([bin(int(x)).replace("0b", "") for x in date.split("-")])


def main():
    sol = Solution()

    date = "2080-02-29"
    print(sol.convertDateToBinary(date))

    date = "1900-01-01"
    print(sol.convertDateToBinary(date))

    pass


if __name__ == "__main__":
    main()
