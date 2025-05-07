#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
problem: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/1628127727/
"""


class Solution:
    # def maxDepth(self, s: str) -> int:
    def maxDepth(self, s):
        stack = []
        count = 0
        max_count = 0

        for i in range(len(s)):
            curr = s[i]

            if curr == "(":
                stack.append(curr)
                count += 1

            if curr == ")":
                if len(stack) > 0:
                    stack.pop()
                    max_count = max(max_count, count)
                    count -= 1

        return max_count


def main():
    sol = Solution()

    s = "(1+(2*3)+((8)/4))+1"
    print(sol.maxDepth(s))

    s = "(1)+((2))+(((3)))"
    print(sol.maxDepth(s))

    s = "()(())((()()))"
    print(sol.maxDepth(s))

    pass


if __name__ == "__main__":
    main()
