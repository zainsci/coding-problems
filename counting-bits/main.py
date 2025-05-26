#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/counting-bits/
problem: https://leetcode.com/problems/counting-bits/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/counting-bits/submissions/1645030868/
"""


class Solution:
    # def countBits(self, n: int) -> List[int]:
    def countBits(self, n):
        return [x.bit_count() for x in range(n+1)]


def main():
    sol = Solution()

    n = 2
    print(sol.countBits(n))

    n = 5
    print(sol.countBits(n))

    pass


if __name__ == "__main__":
    main()
