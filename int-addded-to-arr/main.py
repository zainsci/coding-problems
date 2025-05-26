#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-the-integer-added-to-array-i/
problem: https://leetcode.com/problems/find-the-integer-added-to-array-i/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-the-integer-added-to-array-i/submissions/1645352085/
"""


class Solution:
    # def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
    def addedInteger(self, nums1, nums2):
        return min(nums2)-min(nums1)
        return (sum(nums2)-sum(nums1))//len(nums1)


def main():
    sol = Solution()

    nums1 = [2, 6, 4], nums2 = [9, 7, 5]
    print(sol.addedInteger(nums1, nums2))

    nums1 = [10], nums2 = [5]
    print(sol.addedInteger(nums1, nums2))

    nums1 = [1, 1, 1, 1], nums2 = [1, 1, 1, 1]
    print(sol.addedInteger(nums1, nums2))

    pass


if __name__ == "__main__":
    main()
