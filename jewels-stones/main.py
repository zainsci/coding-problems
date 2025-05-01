#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/jewels-and-stones/
problem: https://leetcode.com/problems/jewels-and-stones/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/jewels-and-stones/submissions/1622666861/
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        types = Counter(stones)
        total = 0

        for jewel in jewels:
            total += types[jewel]

        return total


def main():
    sol = Solution()

    jewels = "aA"
    stones = "aAAbbbb"
    print(sol.numJewelsInStones(jewels, stones))

    jewels = "z"
    stones = "ZZ"
    print(sol.numJewelsInStones(jewels, stones))

    pass


if __name__ == "__main__":
    main()
