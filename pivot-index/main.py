#! /bin/python3

"""
source: https://leetcode.com/problems/find-pivot-index/
problem: https://leetcode.com/problems/find-pivot-index/
type: easy
site: LeetCode
"""


class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    def pivotIndex(self, nums):
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]

        return -1


def main():
    sol = Solution()
    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [1, 2, 3]
    nums = [2, 1, -1]
    print(sol.pivotIndex(nums))


if __name__ == "__main__":
    main()
