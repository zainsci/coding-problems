#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-if-digit-game-can-be-won/
problem: https://leetcode.com/problems/find-if-digit-game-can-be-won/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-if-digit-game-can-be-won/submissions/1646840986/
"""


class Solution:
    # def canAliceWin(self, nums: List[int]) -> bool:
    def canAliceWin(self, nums):
        ups, downs = 0, 0

        for num in nums:
            if num >= 10:
                ups += num
            else:
                downs += num

        return ups != downs


def main():
    sol = Solution()

    nums = [1, 2, 3, 4, 10]
    print(sol.canAliceWin(nums))

    nums = [1, 2, 3, 4, 5, 14]
    print(sol.canAliceWin(nums))

    nums = [5, 5, 5, 25]
    print(sol.canAliceWin(nums))

    pass


if __name__ == "__main__":
    main()
