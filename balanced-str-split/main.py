#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/split-a-string-in-balanced-strings/
problem: https://leetcode.com/problems/split-a-string-in-balanced-strings/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/1623070542/ 
"""


class Solution:
    # def balancedStringSplit(self, s: str) -> int:
    def balancedStringSplit(self, s):
        count = 0

        ls = 0
        rs = 0

        for i in range(len(s)):
            curr = s[i]

            if curr == "L":
                ls += 1
            else:
                rs += 1

            if ls == rs:
                count += 1
                ls = 0
                rs = 0

        return count


def main():
    sol = Solution()

    s = "RLRRLLRLRL"
    print(sol.balancedStringSplit(s))

    s = "RLRRRLLRLL"
    print(sol.balancedStringSplit(s))

    s = "LLLLRRRR"
    print(sol.balancedStringSplit(s))

    pass


if __name__ == "__main__":
    main()
