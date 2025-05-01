#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
problem: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/submissions/1622673365/
"""


class Solution:
    # def finalValueAfterOperations(self, operations: List[str]) -> int:
    def finalValueAfterOperations(self, operations):
        total = 0
        for ops in operations:
            if ops[1] == "-":
                total -= 1
            else:
                total += 1

        return total


def main():
    sol = Solution()
    operations = ["--X", "X++", "X++"]
    print(sol.finalValueAfterOperations(operations))

    operations = ["++X", "++X", "X++"]
    print(sol.finalValueAfterOperations(operations))

    operations = ["X++", "++X", "--X", "X--"]
    print(sol.finalValueAfterOperations(operations))

    pass


if __name__ == "__main__":
    main()
