#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-the-number-of-good-pairs-i/submissions/1626438294/
problem: https://leetcode.com/problems/find-the-number-of-good-pairs-i/submissions/1626438294/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-the-number-of-good-pairs-i/submissions/1626438294/
"""


class Solution:
    # def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
    def numberOfPairs(self, nums1, nums2, k):
        count = 0

        for i in nums1:
            for j in nums2:
                if i % (j*k) == 0:
                    count += 1

        return count


def main():
    sol = Solution()

    nums1 = [1, 3, 4]
    nums2 = [1, 3, 4]
    k = 1
    print(sol.numberOfPairs(nums1, nums2, k))

    nums1 = [1, 2, 4, 12]
    nums2 = [2, 4]
    k = 3
    print(sol.numberOfPairs(nums1, nums2, k))

    pass


if __name__ == "__main__":
    main()
