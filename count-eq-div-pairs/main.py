#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
problem: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/submissions/1628153698/
"""


class Solution:
    # def countPairs(self, nums: List[int], k: int) -> int:
    def countPairs(self, nums, k):
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and ((i * j) % k) == 0:
                    count += 1

        return count


def main():
    sol = Solution()
    nums = [3, 1, 2, 2, 2, 1, 3]
    k = 2
    print(sol.countPairs(nums, k))

    nums = [1, 2, 3, 4]
    k = 1
    print(sol.countPairs(nums, k))

    pass


if __name__ == "__main__":
    main()
