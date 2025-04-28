#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
problem: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/1620601895/
"""


class Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    def smallerNumbersThanCurrent(self, nums):
        count = [0 for _ in nums]
        nums_sorted = sorted(nums)

        for i in range(len(nums)):
            count[i] += nums_sorted.index(nums[i])

        return count


def main():
    sol = Solution()

    nums = [8, 1, 2, 2, 3]
    print(sol.smallerNumbersThanCurrent(nums))

    nums = [6, 5, 4, 8]
    print(sol.smallerNumbersThanCurrent(nums))

    nums = [7, 7, 7, 7]
    print(sol.smallerNumbersThanCurrent(nums))


if __name__ == "__main__":
    main()
