#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
problem: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/submissions/1668060828/
"""


class Solution:
    # def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    def divideArray(self, nums, k):
        nums.sort()
        out = []

        for i in range(0, len(nums), 3):
            if nums[i+2]-nums[i] > k:
                return []

            out.append(nums[i:i+3])

        return out


def main():
    sol = Solution()

    nums = [1, 3, 4, 8, 7, 9, 3, 5, 1]
    k = 2
    print(sol.divideArray(nums, k))

    nums = [2, 4, 2, 2, 5, 2]
    k = 2
    print(sol.divideArray(nums, k))

    nums = [4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11]
    k = 14
    print(sol.divideArray(nums, k))

    pass


if __name__ == "__main__":
    main()
