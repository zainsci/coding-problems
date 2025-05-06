#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/counting-words-with-a-given-prefix/
problem: https://leetcode.com/problems/counting-words-with-a-given-prefix/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/counting-words-with-a-given-prefix/submissions/1627323404/
"""


class Solution:
    # def prefixCount(self, words: List[str], pref: str) -> int:
    def prefixCount(self, words, pref):
        count = 0

        for word in words:
            if word.startswith(pref):
                count += 1

        return count


def main():
    sol = Solution()

    words = ["pay", "attention", "practice", "attend"]
    pref = "at"
    print(sol.prefixCount(words, pref))

    words = ["leetcode", "win", "loops", "success"]
    pref = "code"
    print(sol.prefixCount(words, pref))

    pass


if __name__ == "__main__":
    main()
