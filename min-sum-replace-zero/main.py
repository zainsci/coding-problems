#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
problem: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/submissions/1632935988/
"""


class Solution:
    # def minSum(self, nums1: List[int], nums2: List[int]) -> int:
    def minSum(self, nums1, nums2):

        n1_sum, n1_zeros = sum(nums1), nums1.count(0)
        n2_sum, n2_zeros = sum(nums2), nums2.count(0)

        if n1_sum == n2_sum and (n1_zeros+n2_zeros) == 0:
            return n1_sum

        if min(nums1) > 0 and min(nums2) > 0:
            return -1

        if n1_zeros == 0:
            if n2_zeros + n2_sum > n1_sum:
                return -1

        if n2_zeros == 0:
            if n1_zeros + n1_sum > n2_sum:
                return -1

        if n1_sum + n1_zeros > n2_sum + n2_zeros:
            return n1_sum + n1_zeros
        elif n1_sum + n1_zeros < n2_sum + n2_zeros:
            return n2_sum + n2_zeros

        return max(n1_sum, n2_sum) + min(n1_zeros, n2_zeros)


def main():
    sol = Solution()

    nums1 = [3, 2, 0, 1, 0]
    nums2 = [6, 5, 0]
    print(sol.minSum(nums1, nums2))

    nums1 = [2, 0, 2, 0]
    nums2 = [1, 4]
    print(sol.minSum(nums1, nums2))

    nums1 = [0, 7, 28, 17, 18]
    nums2 = [1, 2, 6, 26, 1, 0, 27, 3, 0, 30]
    print(sol.minSum(nums1, nums2))

    nums1 = [0, 17, 20, 17, 5, 0, 14, 19, 7, 8, 16, 18, 6]
    nums2 = [21, 1, 27, 19, 2, 2, 24, 21, 16,
             1, 13, 27, 8, 5, 3, 11, 13, 7, 29, 7]
    print(sol.minSum(nums1, nums2))

    nums1 = [2, 0, 2, 0]
    nums2 = [1, 4]
    print(sol.minSum(nums1, nums2))

    nums1 = [1, 2, 3, 2]
    nums2 = [1, 4, 3]
    print(sol.minSum(nums1, nums2))

    pass


if __name__ == "__main__":
    main()
