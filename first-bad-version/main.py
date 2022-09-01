#! /bin/python3

"""
source: https://leetcode.com/problems/first-bad-version/
problem: https://leetcode.com/problems/first-bad-version/
type: easy
site: LeetCode
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def find_good_ver(n, s, e):
    mid = (s + e) // 2
    if s > e:
        return mid

    if isBadVersion(mid) and not isBadVersion(mid-1):
        return mid

    if not isBadVersion(mid):
        return find_good_ver(n, mid+1, e)
    if isBadVersion(mid):
        return find_good_ver(n, s, mid-1)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        return find_good_ver(n, 0, n)
