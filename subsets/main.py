#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/subsets/
problem: https://leetcode.com/problems/subsets/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/subsets/submissions/1645892861/
"""


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return res


def main():
    sol = Solution()

    nums = [1, 2, 3]
    nums = [0]

    print()
    pass


if __name__ == "__main__":
    main()
