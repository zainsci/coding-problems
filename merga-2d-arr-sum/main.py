#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
problem: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/submissions/1642465230/
"""


class Solution:
    # def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    def mergeArrays(self, nums1, nums2):
        ans = {x[0]: x[1] for x in nums1}
        for x in nums2:
            key, val = x
            ans[key] = ans.get(key, 0)+val

        return sorted([[key, val] for key, val in ans.items()])


def main():
    sol = Solution()

    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    print(sol.mergeArrays(nums1, nums2))

    nums1 = [[2, 4], [3, 6], [5, 5]]
    nums2 = [[1, 3], [4, 3]]
    print(sol.mergeArrays(nums1, nums2))

    pass


if __name__ == "__main__":
    main()
