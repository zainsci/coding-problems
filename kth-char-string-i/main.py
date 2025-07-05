#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
problem: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
type: Easy 
site: LeetCode
submission: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/submissions/1687571080/
"""


class Solution:
    # def kthCharacter(self, k: int) -> str:
    def kthCharacter(self, k):
        s = "a"
        while len(s) < k:
            s = s + "".join([chr(ord(i)+1) for i in s])

        return s[k-1]


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
