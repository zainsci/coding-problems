#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/semi-ordered-permutation/description/
problem: https://leetcode.com/problems/semi-ordered-permutation/description/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/semi-ordered-permutation/submissions/1795832366/
"""


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        xi, yi = nums.index(min(nums)), nums.index(max(nums))
        n = len(nums)

        return xi + (n - yi - 1) if xi < yi else xi + (n - yi - 1) - 1


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
