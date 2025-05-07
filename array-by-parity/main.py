#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/transform-array-by-parity/
problem: https://leetcode.com/problems/transform-array-by-parity/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/transform-array-by-parity/submissions/1627945816/
"""


class Solution:
    # def transformArray(self, nums: List[int]) -> List[int]:
    def transformArray(self, nums):
        return sorted([
            0 if x % 2 == 0 else 1 for x in nums
        ])


def main():
    sol = Solution()

    nums = [4, 3, 2, 1]
    print(sol.transformArray(nums))

    nums = [1, 5, 1, 4, 2]
    print(sol.transformArray(nums))

    pass


if __name__ == "__main__":
    main()
