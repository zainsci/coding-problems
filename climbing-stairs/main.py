#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/climbing-stairs/
problem: https://leetcode.com/problems/climbing-stairs/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/climbing-stairs/submissions/1628716333/
"""


class Solution:
    # def climbStairs(self, n: int) -> int:
    def climbStairs(self, n):
        return self .climbStairsMemo(n, [None for _ in range(n+1)])

    def climbStairsMemo(self, n, memo):
        if memo[n] is not None:
            return memo[n]
        if n in [1, 2, 3]:
            return n

        res = self.climbStairsMemo(n-1, memo) + self.climbStairsMemo(n-2, memo)
        memo[n] = res

        return res


def main():
    sol = Solution()

    n = 2
    print(sol.climbStairs(n))

    n = 3
    print(sol.climbStairs(n))

    n = 44
    print(sol.climbStairs(n))

    pass


if __name__ == "__main__":
    main()
