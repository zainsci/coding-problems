#!/usr/bin/env python3
from collections import deque

"""
source: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
problem: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/1647913031/
"""


class Solution:
    # def maxCoins(self, piles: List[int]) -> int:
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        return sum(piles[x] for x in range(1, (len(piles)//3)*2, 2))


def main():
    sol = Solution()

    piles = [2, 4, 1, 2, 7, 8]
    print(sol.maxCoins(piles))

    piles = [2, 4, 5]
    print(sol.maxCoins(piles))

    piles = [9, 8, 7, 6, 5, 1, 2, 3, 4]
    print(sol.maxCoins(piles))

    pass


if __name__ == "__main__":
    main()
