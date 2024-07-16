#! /bin/python3

"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
type: easy
site: LeetCode
"""


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        idx = 1
        count = 0

        if len(nums) in [0, 1]:
            return len(nums)

        while idx < len(nums):
            if nums[idx] == nums[idx-1]:
                nums.pop(idx)
            else:
                idx += 1

        return len(nums)


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol = Solution().removeDuplicates(nums)
    print(sol)


if __name__ == "__main__":
    main()
