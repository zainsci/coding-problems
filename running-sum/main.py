#! /bin/python3

"""
source: https://leetcode.com/problems/running-sum-of-1d-array
problem: https://leetcode.com/problems/running-sum-of-1d-array
type: easy
site: LeetCode
"""


class Solution:
    # def runningSum(self, nums: List[int]) -> List[int]:
    def runningSum(self, nums):
        new_arr = []
        total = 0
        for i in nums:
            total += i
            new_arr.append(total)
        return new_arr

    # runningSum with Recursion
    # def runningSum(self, nums: List[int]) -> List[int]:
    def runningSum_recursion(self, nums):
        if len(nums) == 1:
            return nums

        next_val = self.runningSum_recursion(nums[:len(nums)-1])
        total = 0
        for i in nums:
            total += i
        new_arr = [x for x in next_val]
        new_arr.append(total)
        return new_arr


def main():
    sol = Solution()
    nums = [1, 1, 1, 1, 1]
    print(sol.runningSum(nums))
    print(sol.runningSum_recursion(nums))


if __name__ == "__main__":
    main()
