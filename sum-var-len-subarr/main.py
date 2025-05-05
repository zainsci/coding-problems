#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def subarraySum(self, nums: List[int]) -> int:
    def subarraySum(self, nums):
        count = 0

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            count += sum(nums[start:i+1])

        return count


def main():
    sol = Solution()

    nums = [2, 3, 1]
    print(sol.subarraySum(nums))

    nums = [3, 1, 1, 2]
    print(sol.subarraySum(nums))

    nums = [3, 1, 5]
    print(sol.subarraySum(nums))

    pass


if __name__ == "__main__":
    main()
