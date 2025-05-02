#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
problem: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/submissions/1623956777/
"""


class Solution:
    # def minOperations(self, nums: List[int], k: int) -> int:
    def minOperations(self, nums, k):
        return sum(nums) % k


def main():
    sol = Solution()

    nums = [3, 9, 7], k = 5
    print(sol.minOperations(nums, k))

    nums = [4, 1, 3], k = 4
    print(sol.minOperations(nums, k))

    nums = [3, 2], k = 6
    print(sol.minOperations(nums, k))

    print()
    pass


if __name__ == "__main__":
    main()
