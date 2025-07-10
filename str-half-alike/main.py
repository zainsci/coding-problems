#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/determine-if-string-halves-are-alike/
problem: https://leetcode.com/problems/determine-if-string-halves-are-alike/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/1693511889/
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        left, right = s[:n], s[n:]
        lc, rc = 0, 0
        vowels = "aeiouAEIOU"

        for i in range(n):
            if left[i] in vowels:
                lc += 1
            if right[i] in vowels:
                rc += 1

        return lc == rc


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
