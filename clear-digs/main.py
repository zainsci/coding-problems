#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/clear-digits/
problem: https://leetcode.com/problems/clear-digits/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/clear-digits/submissions/1637497868/
"""


class Solution:
    # def clearDigits(self, s: str) -> str:
    def clearDigits(self, s):
        ans = []

        for i in range(len(s)):
            if s[i].isdigit():
                ans.pop()
            else:
                ans.append(s[i])

        return "".join(ans)


def main():
    sol = Solution()

    s = "abc"
    print(sol.clearDigits(s))

    s = "cb34"
    print(sol.clearDigits(s))

    pass


if __name__ == "__main__":
    main()
