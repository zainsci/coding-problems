#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
problem: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/submissions/1647771632/
"""


class Solution:
    # def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    def largestSumAfterKNegations(self, nums, k):

        for i in range(k):
            n = min(nums)
            idx = nums.index(n)
            nums[idx] = -n

        return sum(nums)


def main():
    sol = Solution()

    nums = [4, 2, 3]
    k = 1
    print(sol.largestSumAfterKNegations(nums, k))

    nums = [3, -1, 0, 2]
    k = 3
    print(sol.largestSumAfterKNegations(nums, k))

    nums = [2, -3, -1, 5, -4]
    k = 2
    print(sol.largestSumAfterKNegations(nums, k))

    nums = [-2, 9, 9, 8, 4]
    k = 5
    print(sol.largestSumAfterKNegations(nums, k))

    pass


if __name__ == "__main__":
    main()
