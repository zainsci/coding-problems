#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/remove-outermost-parentheses/
problem: https://leetcode.com/problems/remove-outermost-parentheses/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/remove-outermost-parentheses/submissions/1626467247/
"""


class Solution:
    # def removeOuterParentheses(self, s: str) -> str:
    def removeOuterParentheses(self, s):
        if s == "":
            return s

        ans = ""
        prim = ""
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
                prim += s[i]
            elif s[i] == ")":
                prim += s[i]
                stack.pop()

                if not len(stack) == 0:
                    continue

                ans += prim[1:-1]
                prim = ""

        return ans


def main():
    sol = Solution()

    s = "(()())(())"
    print(sol.removeOuterParentheses(s))

    s = "(()())(())(()(()))"
    print(sol.removeOuterParentheses(s))

    s = "()()"
    print(sol.removeOuterParentheses(s))

    pass


if __name__ == "__main__":
    main()
