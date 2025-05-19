#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
problem: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/submissions/1638679809/
"""


class Solution:
    # def numOfStrings(self, patterns: List[str], word: str) -> int:
    def numOfStrings(self, patterns, word):
        return sum([1 if x in word else 0 for x in patterns])


def main():
    sol = Solution()

    patterns = ["a", "abc", "bc", "d"]
    word = "abc"
    print(sol.numOfStrings(patterns, word))

    patterns = ["a", "b", "c"]
    word = "aaaaabbbbb"
    print(sol.numOfStrings(patterns, word))

    patterns = ["a", "a", "a"]
    word = "ab"
    print(sol.numOfStrings(patterns, word))
    pass


if __name__ == "__main__":
    main()
