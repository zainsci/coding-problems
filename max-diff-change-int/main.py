#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
problem: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/submissions/1665224500/
"""


class Solution:
    # def maxDiff(self, num: int) -> int:
    def maxDiff(self, num):
        num = str(num)

        for i in num:
            if i != "9":
                m = int(num.replace(i, "9"))
                break
            else:
                m = int(num)

        if num[0] != "1":
            n = int(num.replace(num[0], "1"))
        else:
            for i in range(1, len(num)):
                if num[i] != "0" and num[i] != "1":
                    n = int(num.replace(num[i], "0"))
                    break
                else:
                    n = int(num)

        return m - n


def main():
    sol = Solution()

    num = 555
    print(sol.maxDiff(num))

    num = 9
    print(sol.maxDiff(num))

    pass


if __name__ == "__main__":
    main()
