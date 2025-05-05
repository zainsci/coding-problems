#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sum-multiples/
problem: https://leetcode.com/problems/sum-multiples/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sum-multiples/submissions/1626476885/
"""


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        count = 0

        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                count += i

        return count


def main():
    sol = Solution()
    n = 7
    print(sol.sumOfMultiples(n))

    n = 10
    print(sol.sumOfMultiples(n))

    n = 9
    print(sol.sumOfMultiples(n))

    pass


if __name__ == "__main__":
    main()
