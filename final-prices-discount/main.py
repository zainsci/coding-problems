#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
problem: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/submissions/1635017572/
"""


class Solution:
    # def finalPrices(self, prices: List[int]) -> List[int]:
    def finalPrices(self, prices):
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices


def main():
    sol = Solution()

    prices = [8, 4, 6, 2, 3]
    print(sol.finalPrices(prices))

    prices = [1, 2, 3, 4, 5]
    print(sol.finalPrices(prices))

    prices = [10, 1, 1, 6]
    print(sol.finalPrices(prices))

    pass


if __name__ == "__main__":
    main()
