#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-words-containing-character/
problem: https://leetcode.com/problems/find-words-containing-character/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-words-containing-character/submissions/1635579770/
"""


class Solution:
    # def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    def findWordsContaining(self, words, x):
        ans = []

        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)

        return ans


def main():
    sol = Solution()

    words = ["leet", "code"]
    x = "e"
    print(sol.findWordsContaining(words, x))

    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "a"
    print(sol.findWordsContaining(words, x))

    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "z"
    print(sol.findWordsContaining(words, x))

    pass


if __name__ == "__main__":
    main()
