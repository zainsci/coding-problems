#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sorting-the-sentence/
problem: https://leetcode.com/problems/sorting-the-sentence/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sorting-the-sentence/submissions/1636215176/
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([i[1] for i in sorted({x[-1]: x[:-1]
                                               for x in s.split(" ")}.items(), key=lambda x:  x[0])])


def main():
    sol = Solution()

    s = "is2 sentence4 This1 a3"
    print(sol.sortSentence(s))

    s = "Myself2 Me1 I4 and3"
    print(sol.sortSentence(s))

    pass


if __name__ == "__main__":
    main()
