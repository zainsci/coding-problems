#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
problem: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/submissions/1642272843/
"""


class Solution:
    # def minimumOperations(self, nums: List[int]) -> int:
    def minimumOperations(self, nums):
        if sum(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        if min(nums) == 0:
            return len(set(nums))-1

        return len(set(nums))


def main():
    sol = Solution()

    nums = [1, 5, 0, 3, 5]
    print(sol.minimumOperations(nums))

    nums = [0]
    print(sol.minimumOperations(nums))

    pass


if __name__ == "__main__":
    main()
