#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-number-game/
problem: https://leetcode.com/problems/minimum-number-game/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-number-game/submissions/1645322299/
"""


class Solution:
    # def numberGame(self, nums: List[int]) -> List[int]:
    def numberGame(self, nums):
        ans = []
        nums.sort()

        for i in range(len(nums)//2):
            ans.append(nums[1])
            ans.append(nums[0])
            nums = nums[2:]
        return ans


def main():
    sol = Solution()

    nums = [5, 4, 2, 3]
    print(sol.numberGame(nums))

    nums = [2, 5]
    print(sol.numberGame(nums))

    pass


if __name__ == "__main__":
    main()
