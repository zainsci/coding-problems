#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/di-string-match/
problem: https://leetcode.com/problems/di-string-match/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/di-string-match/submissions/1647092623/
"""


class Solution:
    # def diStringMatch(self, s: str) -> List[int]:
    def diStringMatch(self, s):
        inc, dec = 0, len(s)
        ans = []

        for letter in s:
            if letter == "I":
                ans.append(inc)
                inc += 1
            else:
                ans.append(dec)
                dec -= 1

        ans.append(inc)

        return ans


def main():
    sol = Solution()
    s = "IDID"
    print(sol.diStringMatch(s))

    s = "III"
    print(sol.diStringMatch(s))

    s = "DDI"
    print(sol.diStringMatch(s))

    pass


if __name__ == "__main__":
    main()
