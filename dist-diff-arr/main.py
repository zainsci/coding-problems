#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-the-distinct-difference-array/
problem: https://leetcode.com/problems/find-the-distinct-difference-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-the-distinct-difference-array/submissions/1640654603/
"""


class Solution:
    # def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
    def distinctDifferenceArray(self, nums):
        return [len(set(nums[:x]))-len(set(nums[x:]))
                for x in range(1, len(nums)+1)]


def main():
    sol = Solution()

    nums = [1, 2, 3, 4, 5]
    print(sol.distinctDifferenceArray(nums))

    nums = [3, 2, 3, 4, 2]
    print(sol.distinctDifferenceArray(nums))

    pass


if __name__ == "__main__":
    main()
