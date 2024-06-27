#! /bin/python3

"""
source: https://leetcode.com/problems/reverse-vowels-of-a-string/
problem: https://leetcode.com/problems/reverse-vowels-of-a-string/
type: Easy
site: LeetCode
"""

VOWELS = "aeiouAEIOU"


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = []

        for i in range(len(s)):
            if s[i] in VOWELS:
                vowels.append(s[i])
                s[i] = "_"
        for i in range(len(s)):
            if s[i] == "_":
                v = vowels.pop()
                s[i] = v

        return "".join(s)


def main():
    sol = Solution()

    s = "hello"
    print(sol.reverseVowels(s))

    s = "leetcode"
    print(sol.reverseVowels(s))


if __name__ == "__main__":
    main()
