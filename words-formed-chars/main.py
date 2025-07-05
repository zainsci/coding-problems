#!/usr/bin/env python3
from collections import Counter


"""
source: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
problem: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/submissions/1687620986/
"""


class Solution:
    # def countCharacters(self, words: List[str], chars: str) -> int:
    def countCharacters(self, words, chars):
        count = sum(len(word) for word in words)
        freq = Counter(chars)

        for word in words:
            word_freq = Counter(word)

            for key, val in word_freq.items():
                if val > freq[key]:
                    count -= len(word)
                    break

        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
