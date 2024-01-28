#! /bin/python3

"""
source: https://leetcode.com/problems/remove-element/
problem: https://leetcode.com/problems/remove-element/description/
type: easy
site: LeetCode
"""


class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1

        return count


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 3
    sol = Solution().removeElement(nums, val)
    print(sol)


if __name__ == "__main__":
    main()
