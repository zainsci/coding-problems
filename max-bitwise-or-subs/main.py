#!/usr/bin/env python3
from functools import reduce
import operator

"""
source: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
problem: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/submissions/1643349286/
"""


class Solution:
    # def countMaxOrSubsets(self, nums: List[int]) -> int:
    def countMaxOrSubsets(self, nums):
        subs = []
        res = []

        def backtrack(start, path):
            subs.append(path[:])
            res.append(reduce(operator.or_, path, 0))

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return res.count(max(res))


def main():
    sol = Solution()

    nums = [3, 1]
    print(sol.countMaxOrSubsets(nums))

    nums = [2, 2, 2]
    print(sol.countMaxOrSubsets(nums))

    nums = [3, 2, 1, 5]
    print(sol.countMaxOrSubsets(nums))

    pass


if __name__ == "__main__":
    main()
