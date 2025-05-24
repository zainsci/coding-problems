#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/partition-array-according-to-given-pivot/
problem: https://leetcode.com/problems/partition-array-according-to-given-pivot/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/partition-array-according-to-given-pivot/submissions/1643313273/
"""


class Solution:
    # def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    def pivotArray(self, nums, pivot):
        left, mid, right = [], [], []

        for i in nums:
            if i > pivot:
                right.append(i)
            elif i < pivot:
                left.append(i)
            else:
                mid.append(i)

        return left+mid+right


def main():
    sol = Solution()

    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    print(sol.pivotArray(nums, pivot))

    nums = [-3, 4, 3, 2]
    pivot = 2
    print(sol.pivotArray(nums, pivot))

    pass


if __name__ == "__main__":
    main()
