#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/submissions/1687609262/
"""


class Solution:
    # def minimumOperations(self, nums: List[int]) -> int:
    def minimumOperations(self, nums):
        count = 0
        if len(nums) == len(set(nums)):
            return count

        for i in range(0, len(nums), 3):
            curr = nums[i+3:]
            count += 1
            if len(curr) == len(set(curr)):
                break

        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
