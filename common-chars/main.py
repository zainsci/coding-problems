#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/find-common-characters/
problem: https://leetcode.com/problems/find-common-characters/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-common-characters/submissions/1642264601/
"""


class Solution:
    # def commonChars(self, words: List[str]) -> List[str]:
    def commonChars(self, words):
        common = set(words[0])
        counter = [Counter(x) for x in words]
        ans = []

        for word in words:
            common = common & set(word)

        for letter in common:
            ans.extend(letter*min(x[letter] for x in counter))

        return ans


def main():
    sol = Solution()

    words = ["bella", "label", "roller"]
    print(sol.commonChars(words))

    words = ["cool", "lock", "cook"]
    print(sol.commonChars(words))

    words = ["bbddabab", "cbcddbdd", "bbcadcab", "dabcacad",
             "cddcacbc", "ccbdbcba", "cbddaccc", "accdcdbb"]
    print(sol.commonChars(words))

    pass


if __name__ == "__main__":
    main()
