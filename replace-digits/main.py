#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/replace-all-digits-with-characters/
problem: https://leetcode.com/problems/replace-all-digits-with-characters/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/replace-all-digits-with-characters/submissions/1638675116/
"""


class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)

        for i in range(len(s)):
            if s[i].isdigit():
                s[i] = chr(ord(s[i-1])+int(s[i]))

        return "".join(s)


def main():
    sol = Solution()

    s = "a1c1e1"
    print(sol.replaceDigits(s))

    s = "a1b2c3d4e"
    print(sol.replaceDigits(s))

    pass


if __name__ == "__main__":
    main()
