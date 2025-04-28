#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/permutation-difference-between-two-strings/
problem: https://leetcode.com/problems/permutation-difference-between-two-strings/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/permutation-difference-between-two-strings/submissions/1620604361/
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        count = 0
        for i in range(len(s)):
            count += abs(i - t.index(s[i]))

        return count


def main():
    sol = Solution()

    s = "abc"
    t = "bac"
    print(sol.findPermutationDifference(s, t))

    s = "abcde"
    t = "edbac"
    print(sol.findPermutationDifference(s, t))


if __name__ == "__main__":
    main()
