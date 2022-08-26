#! /bin/python3

"""
source: https://leetcode.com/problems/is-subsequence
problem: https://leetcode.com/problems/is-subsequence
site: LeetCode
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for letter in s:
            if letter not in t:
                return False
            t = t[t.index(letter)+1:]
        return True


def main():
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
    s = "axc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))


if __name__ == "__main__":
    main()
