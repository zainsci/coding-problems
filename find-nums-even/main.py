#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions/1623633824/
"""


class Solution:
    # def findNumbers(self, nums: List[int]) -> int:
    def findNumbers(self, nums):
        return sum([1 if len(str(x)) % 2 == 0 else 0 for x in nums])


def main():
    sol = Solution()

    nums = [12, 345, 2, 6, 7896]
    print(sol.findNumbers(nums))

    nums = [555, 901, 482, 1771]
    print(sol.findNumbers(nums))

    pass


if __name__ == "__main__":
    main()
