#!/usr/bin/env python3
from functools import reduce

"""
source: https://leetcode.com/problems/xor-operation-in-an-array/
problem: https://leetcode.com/problems/xor-operation-in-an-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/xor-operation-in-an-array/submissions/1623124213/
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)

        a = reduce(lambda x, y: x ^ y, nums, 0)
        return a


def main():
    sol = Solution()

    n = 5, start = 0
    print(sol.xorOperation(n, start))

    n = 4, start = 3
    print(sol.xorOperation(n, start))

    pass


if __name__ == "__main__":
    main()
