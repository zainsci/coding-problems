#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/max-number-of-k-sum-pairs/
problem: https://leetcode.com/problems/max-number-of-k-sum-pairs/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/max-number-of-k-sum-pairs/submissions/1649605033/
"""


class Solution:
    # def maxOperations(self, nums: List[int], k: int) -> int:
    def maxOperations(self, nums, k):
        left, right = 0, len(nums)-1
        count = 0
        nums.sort()

        while left < right:
            total = nums[left] + nums[right]

            if total < k:
                left += 1
            elif total > k:
                right -= 1
            else:
                count += 1
                left += 1
                right -= 1

        return count


def main():
    sol = Solution()

    nums = [1, 2, 3, 4]
    k = 5
    print(sol.maxOperations(nums, k))

    nums = [3, 1, 3, 4, 3]
    k = 6
    print(sol.maxOperations(nums, k))

    pass


if __name__ == "__main__":
    main()
