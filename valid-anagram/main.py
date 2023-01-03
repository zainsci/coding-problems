#! /bin/python3
from collections import Counter

"""
source: https://leetcode.com/problems/valid-anagram/
problem: https://leetcode.com/problems/valid-anagram/
type: easy
site: LeetCode
"""


class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    def isAnagram(self, s, t):
        s = Counter(s)
        t = Counter(t)

        return s == t


def main():
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print(sol.isAnagram(s, t))


if __name__ == "__main__":
    main()
