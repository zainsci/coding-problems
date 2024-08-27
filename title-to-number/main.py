#! /bin/python3


"""
source: https://leetcode.com/problems/excel-sheet-column-number/
problem: https://leetcode.com/problems/excel-sheet-column-number/
type: Easy
site: LeetCode
"""


class Solution:
    # def titleToNumber(self, columnTitle: str) -> int:
    def titleToNumber(self, columnTitle):
        ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = {y: x+1 for x, y in enumerate(ALPHA)}

        if len(columnTitle) == 1:
            return nums[columnTitle]

        colNum = 0
        for i in range(len(columnTitle)-1):
            colNum += (26 ** int(len(columnTitle)-i-1)) * \
                int(nums[columnTitle[i]])
        colNum += nums[columnTitle[-1]]
        return colNum


def main():
    sol = Solution()

    # columnTitle = "A"
    # print(sol.titleToNumber(columnTitle))

    # columnTitle = "AB"
    # print(sol.titleToNumber(columnTitle))

    columnTitle = "ZZ"
    print(sol.titleToNumber(columnTitle))

    columnTitle = "FXSHRXW"  # 2147483647
    print(sol.titleToNumber(columnTitle))

    return


if __name__ == "__main__":
    main()
