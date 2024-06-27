#! /bin/python3


"""
source: https://leetcode.com/problems/move-zeroes/
problem: https://leetcode.com/problems/move-zeroes/
type: Easy
site: LeetCode
"""


class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0

        while i+zeros < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zeros += 1
            else:
                i += 1

        print(nums)


def main():
    sol = Solution()

    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)

    nums = [0]
    sol.moveZeroes(nums)

    return


if __name__ == "__main__":
    main()
