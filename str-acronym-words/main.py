#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
problem: https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/submissions/1637499885/
"""


class Solution:
    # def isAcronym(self, words: List[str], s: str) -> bool:
    def isAcronym(self, words, s):
        return s == "".join([x[0] for x in words])


def main():
    sol = Solution()
    words = ["alice", "bob", "charlie"]
    s = "abc"
    print(sol.isAcronym(words, s))

    words = ["an", "apple"]
    s = "a"
    print(sol.isAcronym(words, s))

    words = ["never", "gonna", "give", "up", "on", "you"]
    s = "ngguoy"
    print(sol.isAcronym(words, s))

    pass


if __name__ == "__main__":
    main()
