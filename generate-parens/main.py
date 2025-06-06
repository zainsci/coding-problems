#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    def generateParenthesis(self, n):
        left = ["(" for i in range(n)]
        right = [")" for i in range(n)]
        ans = []

        for i in range(n):
            for j in range(n):

                ans.append(
                    "".join(left[i:])+"".join(right[j:]) +
                    "".join(left[:i])+"".join(right[:j])
                )

        return ans


def main():
    sol = Solution()

    n = 3
    print(sol.generateParenthesis(n))

    n = 1
    print(sol.generateParenthesis(n))

    pass


if __name__ == "__main__":
    main()
