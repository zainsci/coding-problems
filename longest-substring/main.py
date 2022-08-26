#! /bin/python3

"""
source: https://leetcode.com/problems/longest-substring-without-repeating-characters
problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
type: medium
site: LeetCode
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_s = []
        last_sub_s = []
        i = 0

        while i < len(s):
            if s[i] not in sub_s:
                sub_s.append(s[i])
            else:
                sub_s = sub_s[sub_s.index(s[i])+1:]
                sub_s.append(s[i])

            if len(sub_s) > len(last_sub_s):
                last_sub_s = sub_s

            i += 1

        return len(last_sub_s)


def main():
    s = ["abcabcbb",
         "pwwkew",
         "bbbbb",
         "dvdf",
         "ohvhjdml"]
    sol = Solution()

    for i in s:
        solution = sol.lengthOfLongestSubstring(i)
        print(i, solution)


if __name__ == "__main__":
    main()
