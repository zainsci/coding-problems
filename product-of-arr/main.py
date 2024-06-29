#! /bin/python3
from functools import reduce


"""
source: https://leetcode.com/problems/product-of-array-except-self/
problem: https://leetcode.com/problems/product-of-array-except-self/
type: Medium
site: LeetCode
"""


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        ans = [None for x in range(len(nums))]
        memo = {}
        for i in range(len(nums)):
            key = nums[i]
            if key in memo.keys():
                ans[i] = memo[key]
            else:
                others = nums[:i] + nums[i+1:]
                ans[i] = reduce(lambda x, y: x*y, others)
                memo[key] = ans[i]

        return ans


def main():
    sol = Solution()

    nums = [1, 2, 3, 4]
    print(sol.productExceptSelf(nums))

    nums = [-1, 1, 0, -3, 3]
    print(sol.productExceptSelf(nums))
    return


if __name__ == "__main__":
    main()
