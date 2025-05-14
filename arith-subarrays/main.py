#!/usr/bin/env python3
from functools import reduce

"""
source: https://leetcode.com/problems/arithmetic-subarrays/
problem: https://leetcode.com/problems/arithmetic-subarrays/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/arithmetic-subarrays/submissions/1633674781/
"""


class Solution:
    # def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    def checkArithmeticSubarrays(self, nums, l, r):
        ans = []

        for i in range(len(l)):
            sub = sorted(nums[l[i]:r[i]+1])
            diff = sub[1] - sub[0]
            is_sub = True

            for j in range(len(sub)-1):
                if diff != sub[j+1]-sub[j]:
                    is_sub = False
                    break

            ans.append(is_sub)

        return ans


def main():
    sol = Solution()

    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    print(sol.checkArithmeticSubarrays(nums, l, r))

    nums = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
    l = [0, 1, 6, 4, 8, 7]
    r = [4, 4, 9, 7, 9, 10]
    print(sol.checkArithmeticSubarrays(nums, l, r))

    pass


if __name__ == "__main__":
    main()
