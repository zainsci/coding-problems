#! /bin/python3

"""
source: https://leetcode.com/problems/isomorphic-strings/
problem: https://leetcode.com/problems/isomorphic-strings/
type: easy
site: LeetCode
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        for i in range(len(s)):
            if s[i] not in d.keys():
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            if d[s[i]] != t[i]:
                return False
        return True


def main():
    sol = Solution()
    s = "badc"
    t = "baba"
    print(sol.isIsomorphic(s, t))
    s = "egg"
    t = "add"
    print(sol.isIsomorphic(s, t))
    s = "foo"
    t = "bar"
    print(sol.isIsomorphic(s, t))
    s = "paper"
    t = "title"
    print(sol.isIsomorphic(s, t))


if __name__ == "__main__":
    main()
