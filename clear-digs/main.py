#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/clear-digits/
problem: https://leetcode.com/problems/clear-digits/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/clear-digits/submissions/1637491687/
"""


class Solution:
    # def clearDigits(self, s: str) -> str:
    def clearDigits(self, s):
        s = list(s)
        n = 0

        while n < len(s):
            char = s[n]

            try:
                _ = int(char)
                s.pop(n)
                s.pop(n-1)
                n -= 1

            except ValueError:
                n += 1
                continue

        return "".join(s)


def main():
    sol = Solution()

    s = "abc"
    print(sol.clearDigits(s))

    s = "cb34"
    print(sol.clearDigits(s))

    pass


if __name__ == "__main__":
    main()
