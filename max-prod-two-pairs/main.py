#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
problem: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/submissions/1644771051/
"""


class Solution:
    # def maxProductDifference(self, nums: List[int]) -> int:
    def maxProductDifference(self, nums):
        s = sorted(nums)
        return (s[-1]*s[-2])-(s[0]*s[1])


def main():
    sol = Solution()

    nums = [5, 6, 2, 7, 4]
    print(sol.maxProductDifference(nums))

    nums = [4, 2, 5, 9, 7, 4, 8]
    print(sol.maxProductDifference(nums))

    pass


if __name__ == "__main__":
    main()
