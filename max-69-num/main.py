#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-69-number/
problem: https://leetcode.com/problems/maximum-69-number/
type: Easy
site: LeetCode 
submission: https://leetcode.com/problems/maximum-69-number/submissions/1647391022/
"""


class Solution:
    # def maximum69Number(self, num: int) -> int:
    def maximum69Number(self, num):
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == "6":
                num[i] = "9"
                break
        return int("".join(num))


def main():
    sol = Solution()

    num = 9669
    print(sol.maximum69Number(num))

    num = 9996
    print(sol.maximum69Number(num))

    num = 9999
    print(sol.maximum69Number(num))

    pass


if __name__ == "__main__":
    main()
