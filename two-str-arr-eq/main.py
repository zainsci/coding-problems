#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
problem: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/submissions/1625566407/
"""


class Solution:
    # def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    def arrayStringsAreEqual(self, word1, word2):
        return "".join(word1) == "".join(word2)


def main():
    sol = Solution()

    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(sol.arrayStringsAreEqual(word1, word2))

    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(sol.arrayStringsAreEqual(word1, word2))

    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(sol.arrayStringsAreEqual(word1, word2))

    pass


if __name__ == "__main__":
    main()
