#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
problem: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/1642853345/
"""


class Solution:
    # def minSteps(self, s: str, t: str) -> int:
    def minSteps(self, s, t):
        count_s = Counter(s)
        count_t = Counter(t)
        ans = 0

        for key in count_t.keys():
            if count_t[key] > count_s.get(key, 0):
                ans += count_t[key]-count_s.get(key, 0)

        return ans


def main():
    sol = Solution()

    s = "bab"
    t = "aba"
    print(sol.minSteps(s, t))

    s = "leetcode"
    t = "practice"
    print(sol.minSteps(s, t))

    s = "anagram"
    t = "mangaar"
    print(sol.minSteps(s, t))

    pass


if __name__ == "__main__":
    main()
