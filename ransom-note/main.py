#! /bin/python3


"""
source: https://leetcode.com/problems/ransom-note/
problem: https://leetcode.com/problems/ransom-note/
type: easy
site: LeetCode
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        for letter in ransomNote:
            if not letter in magazine:
                return False
            else:
                magazine.remove(letter)
        return True


def main():
    sol = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(sol.canConstruct(ransomNote, magazine))


if __name__ == '__main__':
    main()
