#! /bin/python3

"""
source: https://leetcode.com/problems/decode-the-message/
problem: https://leetcode.com/problems/decode-the-message/
type: easy
site: LeetCode
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        sub = {}
        a_count = 0
        value = ""

        for letter in key:
            if a_count >= len(alpha):
                continue
            if letter == " ":
                continue

            if letter not in sub.keys():
                sub[letter] = alpha[a_count]
                a_count += 1
            else:
                continue

        for letter in message:
            if letter == " ":
                value += " "
            else:
                value += sub[letter]

        return value


def main():
    sol = Solution()

    key = "thequickbrownfoxjumpsoverthelazydog"
    message = "vkbs bs t suepuv"
    print(sol.decodeMessage(key, message))

    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(sol.decodeMessage(key, message))

    return


if __name__ == "__main__":
    main()
