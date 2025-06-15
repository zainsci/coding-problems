#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-triangular-sum-of-an-array/
problem: https://leetcode.com/problems/find-triangular-sum-of-an-array/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/find-triangular-sum-of-an-array/submissions/1665244406/
"""


class Solution:
    # def triangularSum(self, nums: List[int]) -> int:
    def triangularSum(self, nums):
        temp = nums
        out = []
        res = temp

        while len(res) > 1:
            for i in range(len(temp)-1):
                out.append((temp[i]+temp[i+1]) % 10)
            res = out
            temp = out
            out = []

        return res[0]


def main():
    sol = Solution()

    nums = [1, 2, 3, 4, 5]
    print(sol.triangularSum(sol))

    nums = [5]
    print(sol.triangularSum(sol))

    pass


if __name__ == "__main__":
    main()
