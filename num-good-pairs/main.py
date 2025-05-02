#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-good-pairs/
problem: https://leetcode.com/problems/number-of-good-pairs/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-good-pairs/submissions/1623918500/
"""


class Solution:
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    def numIdenticalPairs(self, nums):
        count = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1

        return count


def main():
    sol = Solution()

    nums = [1, 2, 3, 1, 1, 3]
    print(sol.numIdenticalPairs(nums))

    nums = [1, 1, 1, 1]
    print(sol.numIdenticalPairs(nums))

    nums = [1, 2, 3]
    print(sol.numIdenticalPairs(nums))

    pass


if __name__ == "__main__":
    main()
