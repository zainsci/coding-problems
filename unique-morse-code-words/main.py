#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/unique-morse-code-words/submissions/1629398731/
problem: https://leetcode.com/problems/unique-morse-code-words/submissions/1629398731/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/unique-morse-code-words/submissions/1629398731/
"""


class Solution:
    # def uniqueMorseRepresentations(self, words: List[str]) -> int:
    def uniqueMorseRepresentations(self, words):
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        morse_set = set()

        for word in words:
            morse_word = "".join([MORSE[ord(x)-97] for x in word])
            morse_set.add(morse_word)

        return len(morse_set)


def main():
    sol = Solution()

    words = ["gin", "zen", "gig", "msg"]
    print(sol.uniqueMorseRepresentations(words))

    words = ["a"]
    print(sol.uniqueMorseRepresentations(words))

    pass


if __name__ == "__main__":
    main()
