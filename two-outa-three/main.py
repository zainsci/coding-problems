#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/two-out-of-three/
problem: https://leetcode.com/problems/two-out-of-three/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/two-out-of-three/submissions/1642487166/
"""


class Solution:
    # def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    def twoOutOfThree(self, nums1, nums2, nums3):
        return list((set(nums1) | set(nums2)) & (set(nums2) | set(nums3)) & (set(nums1) | set(nums3)))


def main():
    sol = Solution()

    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]
    print(sol.twoOutOfThree(nums1, nums2, nums3))

    nums1 = [3, 1]
    nums2 = [2, 3]
    nums3 = [1, 2]
    print(sol.twoOutOfThree(nums1, nums2, nums3))

    nums1 = [1, 2, 2]
    nums2 = [4, 3, 3]
    nums3 = [5]
    print(sol.twoOutOfThree(nums1, nums2, nums3))

    pass


if __name__ == "__main__":
    main()
