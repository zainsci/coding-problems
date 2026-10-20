#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/reverse-string-prefix/
problem: https://leetcode.com/problems/reverse-string-prefix/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/reverse-string-prefix/submissions/2177460132/
"""

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1]+s[k:]


def main():
    sol = Solution()

    s = "abcd"
    k = 2
    print(sol.reversePrefix(s, k))

    s = "xyz"
    k = 3
    print(sol.reversePrefix(s, k))

    s = "hey"
    k = 1
    print(sol.reversePrefix(s, k))

if __name__ == "__main__":
    main()
