#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/keyboard-row/
problem: https://leetcode.com/problems/keyboard-row/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/keyboard-row/submissions/1687593052/
"""


class Solution:
    # def findWords(self, words: List[str]) -> List[str]:
    def findWords(self, words):
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        count = []

        for word in words:
            for row in rows:
                if not word[0].lower() in row:
                    continue

                if all(x.lower() in row for x in word):
                    count.append(word)
                    break

        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
