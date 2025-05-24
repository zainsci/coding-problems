#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
problem: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/submissions/1643326792/
"""


class Solution:
    # def minimumOperations(self, nums: List[int]) -> int:
    def minimumOperations(self, nums):
        return sum([0 if x % 3 == 0 else 1 for x in nums])


def main():
    sol = Solution()

    nums = [1, 2, 3, 4]
    print(sol.minimumOperations(nums))

    nums = [3, 6, 9]
    print(sol.minimumOperations(nums))

    pass


if __name__ == "__main__":
    main()
