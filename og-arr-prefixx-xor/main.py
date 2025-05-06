#!/usr/bin/env python3
from functools import reduce
import operator

"""
source: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
problem: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/submissions/1627281971/
"""


class Solution:
    # def findArray(self, pref: List[int]) -> List[int]:
    def findArray(self, pref):
        ans = []
        last = 0

        for i in pref:
            ans.append(last ^ i)
            last = i
        return ans


def main():
    sol = Solution()

    pref = [5, 2, 0, 3, 1]
    print(sol.findArray(pref))

    pref = [13]
    print(sol.findArray(pref))

    pass


if __name__ == "__main__":
    main()
