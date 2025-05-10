#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/divide-array-into-equal-pairs/
problem: https://leetcode.com/problems/divide-array-into-equal-pairs/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/divide-array-into-equal-pairs/submissions/1630282520/
"""


class Solution:
    # def divideArray(self, nums: List[int]) -> bool:
    def divideArray(self, nums):
        if len(nums) % 2 != 0:
            return False

        nums = Counter(nums)

        for count in nums.values():
            if count % 2 != 0:
                return False

        return True


def main():
    sol = Solution()

    # nums = [3, 2, 3, 2, 2, 2]
    # print(sol.divideArray(nums))

    # nums = [1, 2, 3, 4]
    # print(sol.divideArray(nums))

    nums = [9, 10, 9, 14, 1, 3, 1, 14, 8, 9, 9, 7, 13, 8, 7, 14, 8, 13, 7, 7, 2, 9, 4, 1, 2, 15, 5, 10, 9, 7, 8, 20, 13, 3, 5,
            18, 9, 9, 13, 13, 20, 10, 20, 4, 14, 8, 10, 9, 9, 11, 8, 19, 20, 7, 2, 1, 3, 18, 2, 1, 11, 17, 10, 3, 17, 10, 13, 1, 19, 15]
    print(sol.divideArray(nums))

    pass


if __name__ == "__main__":
    main()
