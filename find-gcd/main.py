# !/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
problem: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
type: Easy 
site: LeetCode
submission: https://leetcode.com/problems/find-greatest-common-divisor-of-array/submissions/1693459185/
"""


class Solution:
    # def findGCD(self, nums: List[int]) -> int:
    def findGCD(self, nums):
        a, b = min(nums), max(nums)
        for i in range(b, 1, -1):
            if a % i == 0 and b % i == 0:
                return i


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
