#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
problem: https://leetcode.com/problems/calculate-money-in-leetcode-bank/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/calculate-money-in-leetcode-bank/submissions/1693574758/
"""


class Solution:
    # def totalMoney(self, n: int) -> int:
    def totalMoney(self, n):
        count = 0
        curr = 0

        for i in range(1, n+1):
            count += curr + (7 if i % 7 == 0 else i % 7)
            if i % 7 == 0:
                curr += 1

        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
