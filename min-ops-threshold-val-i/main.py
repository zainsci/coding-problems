#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
problem: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/submissions/1625562122/
"""


class Solution:
    # def minOperations(self, nums: List[int], k: int) -> int:
    def minOperations(self, nums, k):
        count = 0

        for i in range(len(nums)):
            if nums[i] < k:
                count += 1

        return count


def main():
    sol = Solution()

    nums = [2, 11, 10, 1, 3]
    k = 10
    print(sol.minOperations(nums, k))

    nums = [1, 1, 2, 4, 9]
    k = 1
    print(sol.minOperations(nums, k))

    pass


if __name__ == "__main__":
    main()
