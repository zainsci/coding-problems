#! /bin/python3


"""
source: https://leetcode.com/problems/merge-strings-alternately/
problem: https://leetcode.com/problems/merge-strings-alternately/
type: Easy
site: LeetCode
"""


class Solution:
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    def mergeAlternately(self, word1, word2):
        out = ""
        small = word1 if len(word1) < len(word2) else word2
        big = word1 if len(word1) > len(word2) else word2

        for i in range(len(small)):
            out += word1[i] + word2[i]
        out += big[len(small):]

        return out


def main():
    sol = Solution()
    word1 = "abc"
    word2 = "pqr"
    print(sol.mergeAlternately(word1, word2))

    word1 = "ab"
    word2 = "pqrs"
    print(sol.mergeAlternately(word1, word2))

    word1 = "abcd"
    word2 = "pq"
    print(sol.mergeAlternately(word1, word2))

    return


if __name__ == "__main__":
    main()
