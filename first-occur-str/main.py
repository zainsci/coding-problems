#! /bin/python3

"""
source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
type: Easy
site: LeetCode
"""


class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    def strStr(self, haystack, needle):
        str = haystack[:len(needle)]

        if str == needle:
            return 0

        for i in range(len(needle), len(haystack)):
            str = str[1:]+haystack[i]
            if str == needle:
                return i-len(needle)+1

        return -1


def main():
    sol = Solution()

    haystack = "sadbutsad"
    needle = "sad"
    print(sol.strStr(haystack, needle))

    haystack = "leetcode"
    needle = "leeto"
    print(sol.strStr(haystack, needle))

    haystack = "hello"
    needle = "ll"
    print(sol.strStr(haystack, needle))

    return


if __name__ == "__main__":
    main()
