#!/usr/bin/env python3

from collections import Counter

"""
source: https://leetcode.com/problems/find-lucky-integer-in-an-array/
problem: https://leetcode.com/problems/find-lucky-integer-in-an-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-lucky-integer-in-an-array/submissions/1687536048/
"""


class Solution:
    # def findLucky(self, arr: List[int]) -> int:
    def findLucky(self, arr):
        counter = Counter(arr)
        count = [-1]

        for key, val in counter.items():
            if key == val:
                count.append(key)

        return max(count)


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
