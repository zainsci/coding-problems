#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/find-all-duplicates-in-an-array/
problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/
type: 
site: 
submission: https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/1633998517/
"""


class Solution:
    # def findDuplicates(self, nums: List[int]) -> List[int]:
    def findDuplicates(self, nums):
        nums = Counter(nums)
        ans = []

        for key in nums.keys():
            if nums[key] > 1:
                ans.append(key)

        return ans


def main():
    sol = Solution()

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDuplicates(nums))

    nums = [1, 1, 2]
    print(sol.findDuplicates(nums))

    pass


if __name__ == "__main__":
    main()
