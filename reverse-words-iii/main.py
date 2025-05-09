#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/reverse-words-in-a-string-iii/
problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/1629603691/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split(" ")])


def main():
    sol = Solution()

    s = "Let's take LeetCode contest"
    print(sol.reverseWords(s))

    s = "Mr Ding"
    print(sol.reverseWords(s))

    pass


if __name__ == "__main__":
    main()
