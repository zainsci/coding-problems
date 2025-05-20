#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/snake-in-matrix/submissions/
problem: https://leetcode.com/problems/snake-in-matrix/submissions/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/snake-in-matrix/submissions/1639252736/
"""


class Solution:
    # def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
    def finalPositionOfSnake(self, n, commands):
        pos = 0

        for cmd in commands:
            if cmd == "UP":
                pos -= n
            elif cmd == "DOWN":
                pos += n
            elif cmd == "LEFT":
                pos -= 1
            else:
                pos += 1

        return pos


def main():
    sol = Solution()

    n = 2
    commands = ["RIGHT", "DOWN"]
    print(sol.finalPositionOfSnake(n, commands))

    n = 3
    commands = ["DOWN", "RIGHT", "UP"]
    print(sol.finalPositionOfSnake(n, commands))

    pass


if __name__ == "__main__":
    main()
