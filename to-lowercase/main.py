#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/to-lower-case/
problem: https://leetcode.com/problems/to-lower-case/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/to-lower-case/submissions/1628145811/
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        uppercase = set([chr(x+65) for x in range(26)])
        lowercase = {chr(x+65): chr(97+x) for x in range(26)}

        ans = ""

        for i in s:
            if i in uppercase:
                ans += lowercase[i]
            else:
                ans += i

        return ans


def main():
    sol = Solution()

    s = "Hello"
    print(sol.toLowerCase(s))

    s = "here"
    print(sol.toLowerCase(s))

    s = "LOVELY"
    print(sol.toLowerCase(s))

    pass


if __name__ == "__main__":
    main()
