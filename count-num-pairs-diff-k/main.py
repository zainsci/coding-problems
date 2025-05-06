#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
problem: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/submissions/1627310467/
"""


class Solution:
    # def countKDifference(self, nums: List[int], k: int) -> int:
    def countKDifference(self, nums, k):
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1

        return count


def main():
    sol = Solution()

    nums = [1, 2, 2, 1]
    k = 1
    print(sol.countKDifference(nums, k))

    nums = [1, 3]
    k = 3
    print(sol.countKDifference(nums, k))

    nums = [3, 2, 1, 5, 4],
    k = 2
    print(sol.countKDifference(nums, k))

    pass


if __name__ == "__main__":
    main()
