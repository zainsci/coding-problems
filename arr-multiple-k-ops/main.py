#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
problem: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/submissions/1643924908/
"""


class Solution:
    # def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            n = nums.index(min(nums))
            nums[n] = nums[n]*multiplier

        return nums


def main():
    sol = Solution()

    nums = [2, 1, 3, 5, 6]
    k = 5
    multiplier = 2
    print(sol.getFinalState(nums, k, multiplier))

    nums = [1, 2]
    k = 3
    multiplier = 4
    print(sol.getFinalState(nums, k, multiplier))

    pass


if __name__ == "__main__":
    main()
