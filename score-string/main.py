#! /bin/python3


"""
source: https://leetcode.com/problems/score-of-a-string/
problem: https://leetcode.com/problems/score-of-a-string/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/score-of-a-string/submissions/1380858643/
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0

        for i in range(1, len(s)):
            total += abs(ord(s[i-1])-ord(s[i]))

        return total


def main():
    sol = Solution()

    s = "hello"
    print(sol.scoreOfString(s))

    s = "zaz"
    print(sol.scoreOfString(s))
    return


if __name__ == "__main__":
    main()
