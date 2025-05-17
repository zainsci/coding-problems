#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sorting-the-sentence/
problem: https://leetcode.com/problems/sorting-the-sentence/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sorting-the-sentence/submissions/1636211618/
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        ans = [None for _ in range(len(s))]

        for i in range(len(s)):
            word = s[i]
            ans[int(word[-1])-1] = word[:-1]

        return " ".join(ans)


def main():
    sol = Solution()

    s = "is2 sentence4 This1 a3"
    print(sol.sortSentence(s))

    s = "Myself2 Me1 I4 and3"
    print(sol.sortSentence(s))

    pass


if __name__ == "__main__":
    main()
