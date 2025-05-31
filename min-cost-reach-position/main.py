#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-cost-to-reach-every-position/
problem: https://leetcode.com/problems/minimum-cost-to-reach-every-position/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-cost-to-reach-every-position/submissions/1650059186/
"""


class Solution:
    # def minCosts(self, cost: List[int]) -> List[int]:
    def minCosts(self, cost):
        sm = cost[0]
        ans = []

        for s in cost:
            if not ans:
                ans.append(s)
                continue
            if s < sm:
                ans.append(s)
                sm = s
            else:
                ans.append(sm)

        return ans


def main():
    sol = Solution()

    cost = [5, 3, 4, 1, 3, 2]
    print(sol.minCosts(cost))

    cost = [1, 2, 4, 6, 7]
    print(sol.minCosts(cost))

    pass


if __name__ == "__main__":
    main()
