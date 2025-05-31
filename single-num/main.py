#!/usr/bin/env python3
from functools import reduce


"""
source: https://leetcode.com/problems/single-number/description/
problem: https://leetcode.com/problems/single-number/description/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/single-number/submissions/1649534060/
"""


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)


def main():
    sol = Solution()

    nums = [2, 2, 1]
    print(sol.singleNumber(nums))

    nums = [4, 1, 2, 1, 2]
    print(sol.singleNumber(nums))

    nums = [1]
    print(sol.singleNumber(nums))

    pass


if __name__ == "__main__":
    main()
