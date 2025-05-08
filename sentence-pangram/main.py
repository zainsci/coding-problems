#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
problem: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/check-if-the-sentence-is-pangram/submissions/1628404646/
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


def main():
    sol = Solution()

    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(sol.checkIfPangram(sentence))

    sentence = "leetcode"
    print(sol.checkIfPangram(sentence))
    pass


if __name__ == "__main__":
    main()
