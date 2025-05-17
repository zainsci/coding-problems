#!/usr/bin/env python3


"""
source: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
problem: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/submissions/1636191594/
"""


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = set("aeiou")
        v_freq = {}
        c_freq = {}

        for i in range(len(s)):
            letter = s[i]
            if letter in vow:
                v_freq[letter] = v_freq.get(letter, 0) + 1
            else:
                c_freq[letter] = c_freq.get(letter, 0) + 1

        return max(v_freq.values(), default=0) + max(c_freq.values(), default=0)


def main():
    sol = Solution()

    s = "successes"
    print(sol.maxFreqSum(s))

    s = "aeiaeia"
    print(sol.maxFreqSum(s))

    pass


if __name__ == "__main__":
    main()
