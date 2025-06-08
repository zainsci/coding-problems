#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/baseball-game/
problem: https://leetcode.com/problems/baseball-game/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/baseball-game/submissions/1658029411/
"""


class Solution:
    # def calPoints(self, operations: List[str]) -> int:
    def calPoints(self, operations):
        arr = []
        ans = 0

        for op in operations:
            if op == "D":
                arr.append(arr[-1]*2)
                ans += arr[-1]

            elif op == "C":
                ans -= arr[-1]
                arr.pop()

            elif op == "+":
                arr.append(arr[-1]+arr[-2])
                ans += arr[-1]

            else:
                arr.append(int(op))
                ans += int(op)

        return ans


def main():
    sol = Solution()

    ops = ["5", "2", "C", "D", "+"]
    print(sol.calPoints(ops))

    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(sol.calPoints(ops))

    ops = ["1", "C"]
    print(sol.calPoints(ops))

    pass


if __name__ == "__main__":
    main()
