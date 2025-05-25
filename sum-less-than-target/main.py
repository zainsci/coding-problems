#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
problem: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/submissions/1643898346/
"""


class Solution:
    # def countPairs(self, nums: List[int], target: int) -> int:
    def countPairs(self, nums, target):
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans


def main():
    sol = Solution()

    nums = [-1, 1, 2, 3, 1]
    target = 2
    print(sol.countPairs(nums, target))

    nums = [-6, 2, 5, -2, -7, -1, 3]
    target = -2
    print(sol.countPairs(nums, target))

    pass


if __name__ == "__main__":
    main()
