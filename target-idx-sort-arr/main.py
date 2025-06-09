#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-target-indices-after-sorting-array/
problem: https://leetcode.com/problems/find-target-indices-after-sorting-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-target-indices-after-sorting-array/submissions/1658407922/
"""


class Solution:
    # def targetIndices(self, nums: List[int], target: int) -> List[int]:
    def targetIndices(self, nums, target):
        idx = []
        nums.sort()

        for i, num in enumerate(nums):
            if num == target:
                idx.append(i)

        return idx


def main():
    sol = Solution()
    nums = [1, 2, 5, 2, 3]
    target = 2
    print(sol.targetIndices(nums, target))

    nums = [1, 2, 5, 2, 3]
    target = 3
    print(sol.targetIndices(nums, target))

    nums = [1, 2, 5, 2, 3]
    target = 5
    print(sol.targetIndices(nums, target))

    pass


if __name__ == "__main__":
    main()
