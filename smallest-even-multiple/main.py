#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/smallest-even-multiple/
problem: https://leetcode.com/problems/smallest-even-multiple/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/smallest-even-multiple/submissions/2177461661/
"""
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n*2


def main():
    sol = Solution()

    n = 5
    print(sol.smallestEvenMultiple(n))

    n = 6
    print(sol.smallestEvenMultiple(n))


if __name__ == "__main__":
    main()
