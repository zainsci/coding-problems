#!/usr/bin/env python3
from functools import reduce


"""
source: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
problem: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sum-of-all-subset-xor-totals/submissions/1623868583/
"""


class Solution:
    # def subsetXORSum(self, nums: List[int]) -> int:
    def subsetXORSum(self, nums):
        n = len(nums)
        num_subsets = 1 << n
        total = 0

        for i in range(num_subsets):

            subset = [nums[j] for j in range(n) if (i & (1 << j))]
            if len(subset):
                total += reduce(lambda x, y: x ^ y, subset, 0)

        return total


def main():
    sol = Solution()

    nums = [1, 3]
    print(sol.subsetXORSum(nums))

    nums = [5, 1, 6]
    print(sol.subsetXORSum(nums))

    nums = [3, 4, 5, 6, 7, 8]
    print(sol.subsetXORSum(nums))

    pass


if __name__ == "__main__":
    main()
