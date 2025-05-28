#!/usr/bin/env python3
from collections import deque


"""
source: https://leetcode.com/problems/lemonade-change/
problem: https://leetcode.com/problems/lemonade-change/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/lemonade-change/submissions/1647067554/
"""


class Solution:
    # def lemonadeChange(self, bills: List[int]) -> bool:
    def lemonadeChange(self, bills):
        change = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            change[bill] += 1

            if bill == 10:
                if change[5] <= 0:
                    return False
                change[5] -= 1

            elif bill == 20:
                if change[10] <= 0:
                    if change[5] <= 2:
                        return False
                    else:
                        change[5] -= 3
                elif change[5] == 0:
                    return False
                else:
                    change[5] -= 1
                    change[10] -= 1

        return True


def main():
    sol = Solution()
    bills = [5, 5, 5, 10, 20]
    print(sol.lemonadeChange(bills))

    bills = [5, 5, 10, 10, 20]
    print(sol.lemonadeChange(bills))

    bills = [10, 10]
    print(sol.lemonadeChange(bills))

    bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
    print(sol.lemonadeChange(bills))

    bills = [5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]
    print(sol.lemonadeChange(bills))  # True

    pass


if __name__ == "__main__":
    main()
