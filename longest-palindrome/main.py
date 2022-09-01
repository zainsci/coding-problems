#! /bin/python3

"""
source: https://leetcode.com/problems/longest-palindrome/
problem: https://leetcode.com/problems/longest-palindrome/
type: easy
site: LeetCode
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        total = 0

        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] = d[i] + 1
            if d[i] % 2 == 0:
                total += 2
                d[i] -= 2

        arr = [x if not x % 2 == 0 else 0 for x in d.values()]
        total += max(arr)

        return total


def main():
    sol = Solution()
    s = "abccccdd"
    # s = "a"
    # s = "ccc"
    print(sol.longestPalindrome(s))


if __name__ == "__main__":
    main()
