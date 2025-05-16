#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
problem: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/submissions/1634033977/
"""


class Solution:
    # def minElement(self, nums: List[int]) -> int:
    def minElement(self, nums):
        return min([int(sum([int(x) for x in str(y)])) for y in nums])


def main():
    sol = Solution()

    nums = [10, 12, 13, 14]
    print(sol.minElement(nums))

    nums = [1, 2, 3, 4]
    print(sol.minElement(nums))

    nums = [999, 19, 199]
    print(sol.minElement(nums))

    pass


if __name__ == "__main__":
    main()
