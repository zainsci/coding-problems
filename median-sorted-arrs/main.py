#! /bin/python3

"""
source: https://leetcode.com/problems/median-of-two-sorted-arrays
problem: https://leetcode.com/problems/median-of-two-sorted-arrays
type: hard
site: LeetCode
"""


class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        new_list = []
        new_list_len = len(nums1) + len(nums2)

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                new_list.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                new_list.append(nums1[i])
                i += 1
            else:
                new_list.append(nums1[i])
                new_list.append(nums2[j])
                i += 1
                j += 1

        while new_list_len > len(new_list):
            if i < len(nums1):
                new_list.append(nums1[i])
                i += 1
            elif j < len(nums2):
                new_list.append(nums2[j])
                j += 1

        mid = new_list_len // 2
        if new_list_len % 2 == 0:
            return (new_list[mid] + new_list[mid-1]) / 2
        else:
            return new_list[mid]


def main():
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(sol.findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(sol.findMedianSortedArrays(nums1, nums2))
    nums1 = [0, 0]
    nums2 = [0, 0]
    print(sol.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
    main()
