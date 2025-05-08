#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
problem: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/submissions/1628842592/
"""


class Solution:
    # def firstPalindrome(self, words: List[str]) -> str:
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word

        return ""


def main():
    sol = Solution()

    words = ["abc", "car", "ada", "racecar", "cool"]
    print(sol.firstPalindrome(words))

    words = ["notapalindrome", "racecar"]
    print(sol.firstPalindrome(words))

    words = ["def", "ghi"]
    print(sol.firstPalindrome(words))

    pass


if __name__ == "__main__":
    main()
