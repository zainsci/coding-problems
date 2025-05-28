#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
problem: https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/submissions/1646866210/
"""


class Solution:
    # def minTimeToType(self, word: str) -> int:
    def minTimeToType(self, word):
        letters = {chr(96+i): i for i in range(1, 27)}
        count = len(word)
        word = "a"+word

        for i in range(1, len(word)):
            dis = abs(letters[word[i-1]] - letters[word[i]])
            if dis > 13:
                count += 26 - dis
            else:
                count += dis

        return count


def main():
    sol = Solution()

    word = "abc"
    print(sol.minTimeToType(word))

    word = "bza"
    print(sol.minTimeToType(word))

    word = "zjpc"
    print(sol.minTimeToType(word))

    pass


if __name__ == "__main__":
    main()
