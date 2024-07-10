#! /bin/python3


"""
source: https://leetcode.com/problems/greatest-common-divisor-of-strings/
problem: https://leetcode.com/problems/greatest-common-divisor-of-strings/
type: Easy
site: LeetCode
"""


class Solution:
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
    		    return ""

        len1, len2 = len(str1), len(str2)
        while len2:
    		    len1, len2 = len2, len1 % len2

        return str1[:len1]


def main():
    sol = Solution()

    str1 = "ABCABC"
    str2 = "ABC"
    print(sol.gcdOfStrings(str1, str2))

    str1 = "ABABAB"
    str2 = "ABAB"
    print(sol.gcdOfStrings(str1, str2))

    str1 = "LEET"
    str2 = "CODE"
    print(sol.gcdOfStrings(str1, str2))

    return


if __name__ == "__main__":
    main()
