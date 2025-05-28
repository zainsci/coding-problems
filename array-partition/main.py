#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/array-partition/
problem: https://leetcode.com/problems/array-partition/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/array-partition/submissions/1646787521/
"""


class Solution:
    # def arrayPairSum(self, nums: List[int]) -> int:
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        return sum(nums[x] for x in range(0, len(nums), 2))


def main():
    sol = Solution()

    nums = [1, 4, 3, 2]
    print(sol.arrayPairSum(nums))

    nums = [6, 2, 6, 5, 1, 2]
    print(sol.arrayPairSum(nums))

    pass


if __name__ == "__main__":
    main()
