#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
problem: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/1633626903/
"""


class Solution:
    # def repeatedNTimes(self, nums: List[int]) -> int:
    def repeatedNTimes(self, nums):
        count = Counter(nums)

        for key in count.keys():
            if count[key] == len(nums)//2:
                return count[key]


def main():
    sol = Solution()

    nums = [1, 2, 3, 3]
    print(sol.repeatedNTimes(nums))

    nums = [2, 1, 2, 5, 3, 2]
    print(sol.repeatedNTimes(nums))

    nums = [5, 1, 5, 2, 5, 3, 5, 4]
    print(sol.repeatedNTimes(nums))
    pass


if __name__ == "__main__":
    main()
