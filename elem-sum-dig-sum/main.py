#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/ 
problem: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/submissions/1627314778/
"""


class Solution:
    # def differenceOfSum(self, nums: List[int]) -> int:
    def differenceOfSum(self, nums):
        elem_sum = sum(nums)
        dig_sum = 0

        for i in nums:
            if i <= 9:
                dig_sum += i
            else:
                for j in str(i):
                    dig_sum += int(j)

        return abs(elem_sum-dig_sum)


def main():
    sol = Solution()

    nums = [1, 15, 6, 3]
    print(sol.differenceOfSum(nums))

    nums = [1, 2, 3, 4]
    print(sol.differenceOfSum(nums))

    pass


if __name__ == "__main__":
    main()
