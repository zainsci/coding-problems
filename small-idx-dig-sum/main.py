#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
problem: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/submissions/1656045348/
"""


class Solution:
    # def smallestIndex(self, nums: List[int]) -> int:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if i == sum(int(x) for x in str(nums[i])):
                return i

        return -1


def main():
    sol = Solution()

    nums = [1, 3, 2]
    print(sol.smallestIndex(nums))

    nums = [1, 10, 11]
    print(sol.smallestIndex(nums))

    nums = [1, 2, 3]
    print(sol.smallestIndex(nums))

    pass


if __name__ == "__main__":
    main()
