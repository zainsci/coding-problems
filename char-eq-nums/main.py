#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
problem: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/submissions/1631355536/
"""


class Solution:
    # def areOccurrencesEqual(self, s: str) -> bool:
    def areOccurrencesEqual(self, s):
        count = Counter(s)

        sorted_vals = count.values()
        if min(sorted_vals) == max(sorted_vals):
            return True

        return False


def main():
    sol = Solution()

    s = "abacbc"
    print(sol.areOccurrencesEqual(s))

    s = "aaabb"
    print(sol.areOccurrencesEqual(s))

    s = "jfdntzwmzrsurunnoezrybmtm"
    print(sol.areOccurrencesEqual(s))

    pass


if __name__ == "__main__":
    main()
