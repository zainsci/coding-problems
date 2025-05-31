#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/max-consecutive-ones-iii/
problem: https://leetcode.com/problems/max-consecutive-ones-iii/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1649646576/
"""


class Solution:
    # def longestOnes(self, nums: List[int], k: int) -> int:
    def longestOnes(self, nums, k):
        left, right, total, zeros, big = 0, 0, 0, 0, 0
        n = len(nums)

        while right < n:
            num = nums[right]
            right += 1

            if num == 1:
                total += 1
            else:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    left += 1
                    zeros -= 1
                else:
                    total -= 1
                    left += 1
            else:
                big = max(big, total+zeros)

        return big


def main():
    sol = Solution()

    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(sol.longestOnes(nums, k))

    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(sol.longestOnes(nums, k))

    nums = [0, 0, 0, 1]
    k = 4
    print(sol.longestOnes(nums, k))

    pass


if __name__ == "__main__":
    main()
