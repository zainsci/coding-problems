#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
problem: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/submissions/1659508437/
"""


class Solution:
    # def maxDifference(self, s: str) -> int:
    def maxDifference(self, s):
        count = Counter(s)

        odd = float("-inf")
        even = float("inf")

        for val in count.values():
            if val & 1:
                odd = max(odd, val)
            else:
                even = min(even, val)

        return odd - even


def main():
    sol = Solution()

    s = "aaaaabbc"
    print(sol.maxDifference(s))

    s = "abcabcab"
    print(sol.maxDifference(s))

    pass


if __name__ == "__main__":
    main()
