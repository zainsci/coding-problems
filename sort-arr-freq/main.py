#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/sort-array-by-increasing-frequency/ 
problem: https://leetcode.com/problems/sort-array-by-increasing-frequency/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sort-array-by-increasing-frequency/submissions/1630276494/
"""


class Solution:
    # def frequencySort(self, nums: List[int]) -> List[int]:
    def frequencySort(self, nums):
        return sorted(nums, key=lambda x: (nums.count(x), -x))


def main():
    sol = Solution()

    nums = [1, 1, 2, 2, 2, 3]
    print(sol.frequencySort(nums))

    nums = [2, 3, 1, 3, 2]
    print(sol.frequencySort(nums))

    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(sol.frequencySort(nums))

    pass


if __name__ == "__main__":
    main()
