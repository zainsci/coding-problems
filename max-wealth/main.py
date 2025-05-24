#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/richest-customer-wealth/
problem: https://leetcode.com/problems/richest-customer-wealth/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/richest-customer-wealth/submissions/1643334395/
"""


class Solution:
    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    def maximumWealth(self, accounts):
        return max(sum(x) for x in accounts)


def main():
    sol = Solution()

    accounts = [[1, 2, 3], [3, 2, 1]]
    print(sol.maximumWealth(accounts))

    accounts = [[1, 5], [7, 3], [3, 5]]
    print(sol.maximumWealth(accounts))

    pass


if __name__ == "__main__":
    main()
