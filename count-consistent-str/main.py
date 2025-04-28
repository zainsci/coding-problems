#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-the-number-of-consistent-strings/
problem: https://leetcode.com/problems/count-the-number-of-consistent-strings/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-the-number-of-consistent-strings/submissions/1620595216/
"""


class Solution:
    # def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    def countConsistentStrings(self, allowed, words):
        count = 0

        for word in words:
            is_allowed = all([True if x in allowed else False for x in word])

            if is_allowed:
                count += 1

        return count


def main():
    sol = Solution()

    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(sol.countConsistentStrings(allowed, words))

    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(sol.countConsistentStrings(allowed, words))

    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    print(sol.countConsistentStrings(allowed, words))


if __name__ == "__main__":
    main()
