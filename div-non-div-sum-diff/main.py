#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
problem: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/submissions/1645854751/
"""


class Solution:
    # def differenceOfSums(self, n: int, m: int) -> int:
    def differenceOfSums(self, n, m):
        return sum(x if x % m != 0 else 0 for x in range(1, n+1)) - sum(x if x % m == 0 else 0 for x in range(1, n+1))


def main():
    sol = Solution()

    n = 10
    m = 3
    print(sol.differenceOfSums(n, m))

    n = 5
    m = 6
    print(sol.differenceOfSums(n, m))

    n = 5
    m = 1
    print(sol.differenceOfSums(n, m))

    pass


if __name__ == "__main__":
    main()
