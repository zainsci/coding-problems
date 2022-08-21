#! /bin/python3

"""
source: https://leetcode.com/problems/two-sum
problem: https://leetcode.com/problems/two-sum/
site: LeetCode
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num in nums and nums.index(second_num) != i:
                return i, nums.index(second_num)


def main():
    nums = [3, 3]
    target = 6
    sol = Solution()
    solution = sol.twoSum(nums, target)
    print(solution)


if __name__ == "__main__":
    main()
