#! /bin/python3


"""
source: https://leetcode.com/problems/binary-search/
problem: https://leetcode.com/problems/binary-search/
type: easy
site: LeetCode
"""


def bin_search(nums, target, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2

    if nums[mid] < target:
        return bin_search(nums, target, mid + 1, end)
    elif nums[mid] > target:
        return bin_search(nums, target, start, mid - 1)
    else:
        return mid


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        return bin_search(nums, target, start, end)


def main():
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(sol.search(nums, target))


if __name__ == "__main__":
    main()
