#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/left-and-right-sum-differences/
problem: https://leetcode.com/problems/left-and-right-sum-differences/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/left-and-right-sum-differences/submissions/1643915507/
"""


class Solution:
    # def leftRightDifference(self, nums: List[int]) -> List[int]:
    def leftRightDifference(self, nums):
        n = len(nums)
        left, right = [0]*n, [0]*n

        for i in range(n):
            left[i] = sum(nums[:i])
            right[n-i-1] = sum(nums[n-i:])

        return [abs(left[x]-right[x]) for x in range(n)]


def main():
    sol = Solution()

    nums = [10, 4, 8, 3]
    print(sol.leftRightDifference(nums))

    nums = [1]
    print(sol.leftRightDifference(nums))

    pass


if __name__ == "__main__":
    main()
