#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/first-letter-to-appear-twice/
problem: https://leetcode.com/problems/first-letter-to-appear-twice/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/first-letter-to-appear-twice/submissions/1627952999/
"""


class Solution:
    # def repeatedCharacter(self, s: str) -> str:
    def repeatedCharacter(self, s):
        check = set()

        for char in s:
            if char not in check:
                check.add(str(char))
            else:
                return char

        return


def main():
    sol = Solution()

    s = "abccbaacz"
    print(sol.repeatedCharacter(s))

    s = "abcdd"
    print(sol.repeatedCharacter(s))

    pass


if __name__ == "__main__":
    main()
