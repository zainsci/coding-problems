#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/min-stack/
problem: https://leetcode.com/problems/min-stack/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/min-stack/submissions/1648828521/
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.mins.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def main():
    # sol = Solution()
    # print()
    pass


if __name__ == "__main__":
    main()
