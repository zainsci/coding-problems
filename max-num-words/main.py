#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
problem: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/submissions/1623870611/
"""


class Solution:
    # def mostWordsFound(self, sentences: List[str]) -> int:
    def mostWordsFound(self, sentences):
        counts = []

        for sentence in sentences:
            counts.append(len(sentence.split(" ")))

        return max(counts)


def main():
    sol = Solution()

    sentences = ["alice and bob love leetcode",
                 "i think so too", "this is great thanks very much"]
    print(sol.mostWordsFound(sentences))

    sentences = ["please wait", "continue to fight", "continue to win"]
    print(sol.mostWordsFound(sentences))

    pass


if __name__ == "__main__":
    main()
