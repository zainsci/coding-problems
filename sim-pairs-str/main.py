#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-pairs-of-similar-strings/
problem: https://leetcode.com/problems/count-pairs-of-similar-strings/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-pairs-of-similar-strings/submissions/1640394650/
"""


class Solution:
    # def similarPairs(self, words: List[str]) -> int:
    def similarPairs(self, words):
        count = 0

        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[i]) == set(words[j]):
                    count += 1

        return count


def main():
    sol = Solution()

    words = ["aba", "aabb", "abcd", "bac", "aabc"]
    print(sol.similarPairs(words))

    words = ["aabb", "ab", "ba"]
    print(sol.similarPairs(words))

    words = ["nba", "cba", "dba"]
    print(sol.similarPairs(words))

    pass


if __name__ == "__main__":
    main()
