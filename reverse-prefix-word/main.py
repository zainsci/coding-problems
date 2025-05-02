#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/reverse-prefix-of-word/
problem: https://leetcode.com/problems/reverse-prefix-of-word/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/reverse-prefix-of-word/submissions/1623939569/
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if ch == word[i]:
                word = word[:i+1][::-1] + word[i+1:]
                break
        return word


def main():
    sol = Solution()

    word = "abcdefd"
    ch = "d"
    print(sol.reversePrefix(word, ch))

    word = "xyxzxe"
    ch = "z"
    print(sol.reversePrefix(word, ch))

    word = "abcd"
    ch = "z"
    print(sol.reversePrefix(word, ch))
    pass


if __name__ == "__main__":
    main()
