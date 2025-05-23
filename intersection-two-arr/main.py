#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/intersection-of-two-arrays/
problem: https://leetcode.com/problems/intersection-of-two-arrays/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/intersection-of-two-arrays/submissions/1642480513/
"""


class Solution:
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


def main():
    sol = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(sol.intersection(nums1, nums2))

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(sol.intersection(nums1, nums2))

    pass


if __name__ == "__main__":
    main()
