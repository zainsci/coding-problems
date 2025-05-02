#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/concatenation-of-array/
problem: https://leetcode.com/problems/concatenation-of-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/concatenation-of-array/submissions/1623909545/
"""


class Solution:
    # def getConcatenation(self, nums: List[int]) -> List[int]:
    def getConcatenation(self, nums):
        return nums+nums


def main():
    sol = Solution()

    nums = [1, 2, 1]
    print(sol.getConcatenation(nums))

    nums = [1, 3, 2, 1]
    print(sol.getConcatenation(nums))

    pass


if __name__ == "__main__":
    main()
