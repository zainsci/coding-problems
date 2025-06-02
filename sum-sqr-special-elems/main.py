#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sum-of-squares-of-special-elements/
problem: https://leetcode.com/problems/sum-of-squares-of-special-elements/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sum-of-squares-of-special-elements/submissions/1652125243/
"""


class Solution:
    # def sumOfSquares(self, nums: List[int]) -> int:
    def sumOfSquares(self, nums):
        return sum(nums[i-1]**2 if len(nums) % i == 0 else 0 for i in range(1, len(nums)+1))


def main():
    sol = Solution()

    nums = [1, 2, 3, 4]
    print(sol.sumOfSquares(nums))

    nums = [2, 7, 1, 19, 18, 3]
    print(sol.sumOfSquares(nums))

    pass


if __name__ == "__main__":
    main()
