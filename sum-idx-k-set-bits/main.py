#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/
problem: https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/submissions/1644808662/
"""


class Solution:
    # def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
    def sumIndicesWithKSetBits(self, nums, k):
        return sum(x if bin(i).count("1") == k else 0 for i, x in enumerate(nums))


def main():
    sol = Solution()

    nums = [5, 10, 1, 5, 2]
    k = 1
    print(sol.  sumIndicesWithKSetBits(nums, k))
    nums = [4, 3, 2, 1]
    k = 2
    print(sol.  sumIndicesWithKSetBits(nums, k))

    pass


if __name__ == "__main__":
    main()
