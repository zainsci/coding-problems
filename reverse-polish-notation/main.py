#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/evaluate-reverse-polish-notation/
problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1648932305/
"""


class Solution:
    # def evalRPN(self, tokens: List[str]) -> int:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)

            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(token))

        return stack[0]


def main():
    sol = Solution()

    tokens = ["2", "1", "+", "3", "*"]
    print(sol.evalRPN(tokens))

    tokens = ["4", "13", "5", "/", "+"]
    print(sol.evalRPN(tokens))

    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    print(sol.evalRPN(tokens))

    pass


if __name__ == "__main__":
    main()
