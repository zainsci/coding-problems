#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
problem: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/1623115085/
"""


class Solution:
    # def subtractProductAndSum(self, n: int) -> int:
    def subtractProductAndSum(self, n):
        n = [int(x) for x in str(n)]

        sumd = sum(n)
        prod = 1
        for i in n:
            prod = i * prod

        return prod - sumd


def main():
    sol = Solution()

    n = 234
    print(sol.subtractProductAndSum(n))

    n = 4421
    print(sol.subtractProductAndSum(n))

    pass


if __name__ == "__main__":
    main()
