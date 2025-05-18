#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/1637450982/
"""


class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums):
        return (sorted(nums)[-1]-1)*(sorted(nums)[-2]-1)


def main():
    sol = Solution()

    nums = [3, 4, 5, 2]
    print(sol.maxProduct(nums))

    nums = [1, 5, 4, 5]
    print(sol.maxProduct(nums))

    nums = [3, 7]
    print(sol.maxProduct(nums))

    pass


if __name__ == "__main__":
    main()
