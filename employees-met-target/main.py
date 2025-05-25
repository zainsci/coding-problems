#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-employees-who-met-the-target/
problem: https://leetcode.com/problems/number-of-employees-who-met-the-target/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-employees-who-met-the-target/submissions/1643894386/
"""


class Solution:
    # def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        return sum(1 if x >= target else 0 for x in hours)


def main():
    sol = Solution()

    hours = [0, 1, 2, 3, 4]
    target = 2
    print(sol.numberOfEmployeesWhoMetTarget(hours, target))

    hours = [5, 1, 4, 2, 2]
    target = 6
    print(sol.numberOfEmployeesWhoMetTarget(hours, target))

    pass


if __name__ == "__main__":
    main()
