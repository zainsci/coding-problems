#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
problem: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/submissions/1642282086/
"""


class Solution:
    # def minOperations(self, nums: List[int], k: int) -> int:
    def minOperations(self, nums, k):
        if min(nums) < k:
            return -1

        if len(nums) == 1:
            if sum(nums) == k:
                return 0
            else:
                return 1

        if min(nums) == k:
            return len(set(nums))-1

        return len(set(nums))


def main():
    sol = Solution()

    nums = [5, 2, 5, 4, 5]
    k = 2
    print(sol.minOperations(nums, k))

    nums = [2, 1, 2]
    k = 2
    print(sol.minOperations(nums, k))

    nums = [9, 7, 5, 3]
    k = 1
    print(sol.minOperations(nums, k))

    pass


if __name__ == "__main__":
    main()
