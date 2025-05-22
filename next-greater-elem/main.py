#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/next-greater-element-i/
problem: https://leetcode.com/problems/next-greater-element-i/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/next-greater-element-i/submissions/1641354439/
"""


class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            next_elem = nums1[i]

            for j in range(idx, len(nums2)):
                if nums2[j] > next_elem:
                    next_elem = nums2[j]
                    break

            if next_elem == nums1[i]:
                ans.append(-1)
            else:
                ans.append(next_elem)

        return ans


def main():
    sol = Solution()

    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(sol.nextGreaterElement(nums1, nums2))

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(sol.nextGreaterElement(nums1, nums2))

    pass


if __name__ == "__main__":
    main()
