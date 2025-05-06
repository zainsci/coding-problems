#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/ 
problem: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/submissions/1627313011/
"""


class Solution:
    # def differenceOfSum(self, nums: List[int]) -> int:
    def differenceOfSum(self, nums):
        elem_sum = sum(nums)
        dig_sum = sum([sum([int(x) for x in str(y)]) for y in nums])
        return abs(elem_sum-dig_sum)


def main():
    sol = Solution()

    nums = [1, 15, 6, 3]
    print(sol.differenceOfSum(nums))

    nums = [1, 2, 3, 4]
    print(sol.differenceOfSum(nums))

    pass


if __name__ == "__main__":
    main()
