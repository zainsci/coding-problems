#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
problem: https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/submissions/1652130804/
"""


class Solution:
    # def minOperations(self, nums: List[int]) -> int:
    def minOperations(self, nums):
        if len(nums) == 1:
            return 0

        arr = nums[:]
        for i in range(1, len(nums)):
            if arr[i-1] >= arr[i]:
                arr[i] += (arr[i-1] - arr[i]) + 1

        return sum(arr) - sum(nums)


def main():
    sol = Solution()

    nums = [1, 1, 1]
    print(sol.minOperations(nums))

    nums = [1, 5, 2, 4, 1]
    print(sol.minOperations(nums))

    pass


if __name__ == "__main__":
    main()
