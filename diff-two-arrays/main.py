#! /bin/python3


"""
source: https://leetcode.com/problems/find-the-difference-of-two-arrays/
problem: https://leetcode.com/problems/find-the-difference-of-two-arrays/
type: Easy
site: LeetCode
"""


class Solution:
    # def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    def findDifference(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        return [list(nums1-nums2), list(nums2-nums1)]


def main():
    sol = Solution()

    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    print(sol.findDifference(nums1, nums2))

    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    print(sol.findDifference(nums1, nums2))

    return


if __name__ == "__main__":
    main()
