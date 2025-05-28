#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/valid-palindrome-ii/
problem: https://leetcode.com/problems/valid-palindrome-ii/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/valid-palindrome-ii/submissions/1646895675/
"""


class Solution:
    # def validPalindrome(self, s: str) -> bool:
    def validPalindrome(self, s):
        def isPal(word):
            return word == word[::-1]

        left, right = 0, len(s)-1
        letterDeleted = False

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                if letterDeleted:
                    return False

                if isPal(s[left:right]):
                    right -= 1
                elif isPal(s[left+1:right+1]):
                    left += 1
                else:
                    return False
                letterDeleted = True

        return True


def main():
    sol = Solution()

    s = "aba"  # True
    print(sol.validPalindrome(s))

    s = "abca"  # True
    print(sol.validPalindrome(s))

    s = "abc"  # False
    print(sol.validPalindrome(s))

    s = "cbbcc"  # True
    print(sol.validPalindrome(s))

    s = "eccer"  # True
    print(sol.validPalindrome(s))

    s = "tebbem"  # False
    print(sol.validPalindrome(s))

    pass


if __name__ == "__main__":
    main()
