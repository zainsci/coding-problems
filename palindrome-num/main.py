#! /bin/python3

"""
source: https://leetcode.com/problems/palindrome-number/
problem: https://leetcode.com/problems/palindrome-number/
site: LeetCode
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        mid = len(x) // 2
        left = None
        right = None

        if len(x) % 2 == 0:
            left = x[:mid]
            right = x[mid:][::-1]
        else:
            left = x[:mid]
            right = x[mid+1:][::-1]

        return True if left == right else False


def main():
    sol = Solution()
    print(sol.isPalindrome(78945654987))
    print(sol.isPalindrome(75357))
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(10))


if __name__ == '__main__':
    main()
