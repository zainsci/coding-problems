#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-arithmetic-triplets/
problem: https://leetcode.com/problems/number-of-arithmetic-triplets/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-arithmetic-triplets/submissions/1627679651/
"""


class Solution:
    # def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    def arithmeticTriplets(self, nums, diff):
        diffs = 0
        sets = set(nums)

        for i in range(len(nums)):
            if nums[i] + diff in sets and nums[i] + 2 * diff in sets:
                diffs += 1

        return diffs


def main():
    sol = Solution()

    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    print(sol.arithmeticTriplets(nums, diff))

    nums = [4, 5, 6, 7, 8, 9]
    diff = 2
    print(sol.arithmeticTriplets(nums, diff))

    nums = [2, 4, 5, 7, 8]
    diff = 1
    print(sol.arithmeticTriplets(nums, diff))

    pass


if __name__ == "__main__":
    main()
