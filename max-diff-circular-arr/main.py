#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
problem: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/submissions/1662140578/
"""


class Solution:
    # def maxAdjacentDistance(self, nums: List[int]) -> int:
    def maxAdjacentDistance(self, nums):
        out = [abs(nums[0]-nums[-1])]

        for i in range(1, len(nums)):
            out.append(abs(nums[i-1] - nums[i]))

        return max(out)


def main():
    sol = Solution()

    nums = [1, 2, 4]
    print(sol.maxAdjacentDistance(nums))

    nums = [-5, -10, -5]
    print(sol.maxAdjacentDistance(nums))

    pass


if __name__ == "__main__":
    main()
