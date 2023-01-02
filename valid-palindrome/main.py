#! /bin/python3

"""
source: https://leetcode.com/problems/valid-palindrome/
problem: https://leetcode.com/problems/valid-palindrome/
type: easy
site: LeetCode
"""


class Solution:
    # def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        s = [item for item in s if item.isalnum()]
        s = "".join(s)
        s = s.lower()
        first, second = s[: len(s) // 2], s[len(s) // 2 :]

        if len(first) != len(second):
            return first == second[1:][::-1]
        else:
            return first == second[::-1]


def main():
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))

    s = " "
    print(sol.isPalindrome(s))


if __name__ == "__main__":
    main()
