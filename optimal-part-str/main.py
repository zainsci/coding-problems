#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/optimal-partition-of-string/
problem: https://leetcode.com/problems/optimal-partition-of-string/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/optimal-partition-of-string/submissions/1633989890/
"""


class Solution:
    # def partitionString(self, s: str) -> int:
    def partitionString(self, s):
        ans = 0
        curr = []

        for i in s:
            if i not in curr:
                curr.append(i)
            else:
                ans += 1
                curr = [i]

        ans += 1
        return ans


def main():
    sol = Solution()

    s = "abacaba"
    print(sol.partitionString(s))

    s = "ssssss"
    print(sol.partitionString(s))

    pass


if __name__ == "__main__":
    main()
