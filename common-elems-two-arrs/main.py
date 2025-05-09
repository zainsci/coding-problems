#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-common-elements-between-two-arrays/
problem: https://leetcode.com/problems/find-common-elements-between-two-arrays/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-common-elements-between-two-arrays/submissions/1629319574/
"""


class Solution:
    # def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def findIntersectionValues(self, nums1, nums2):
        count_1 = 0
        count_2 = 0

        nums1_set = set(nums1)
        nums2_set = set(nums2)

        for i in nums1:
            if i in nums2_set:
                count_1 += 1

        for i in nums2:
            if i in nums1_set:
                count_2 += 1

        return [count_1,  count_2]


def main():
    sol = Solution()

    nums1 = [2, 3, 2]
    nums2 = [1, 2]
    print(sol.findIntersectionValues(nums1, nums2))

    nums1 = [4, 3, 2, 3, 1]
    nums2 = [2, 2, 5, 2, 3, 6]
    print(sol.findIntersectionValues(nums1, nums2))

    pass


if __name__ == "__main__":
    main()
