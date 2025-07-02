#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-common-factors/
problem: https://leetcode.com/problems/number-of-common-factors/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-common-factors/submissions/1684178388/
"""


class Solution:
    # def commonFactors(self, a: int, b: int) -> int:
    def commonFactors(self, a, b) -> int:
        count = 0
        for i in range(1, min(a, b)+1):
            if not a % i and not b % i:
                count += 1
        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
