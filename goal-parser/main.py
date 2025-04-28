#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/goal-parser-interpretation/
problem: https://leetcode.com/problems/goal-parser-interpretation/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/goal-parser-interpretation/submissions/1620590007/
"""


class Solution:
    def interpret(self, command: str) -> str:
        command = list(command)
        i = 0

        while i < len(command):
            if command[i] == "(":
                if command[i+1] == ")":
                    command[i] = "o"
                    command = command[:i+1] + command[i+2:]

                elif command[i+1] == "a":
                    j = i

                    while not command[j] == ")":
                        j += 1
                    command[i] = "a"
                    command[i+1] = "l"
                    command = command[:i+2] + command[i+4:]

            i += 1
        return "".join(command)


def main():
    sol = Solution()

    command = "G()(al)"
    print(sol.interpret(command))

    command = "G()()()()(al)"
    print(sol.interpret(command))

    command = "(al)G(al)()()G"
    print(sol.interpret(command))


if __name__ == "__main__":
    main()
