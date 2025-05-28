#!/usr/bin/env python3
from collections import deque


"""
source: https://leetcode.com/problems/lemonade-change/
problem: https://leetcode.com/problems/lemonade-change/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/lemonade-change/submissions/1646929693/
"""


class Solution:
    # def lemonadeChange(self, bills: List[int]) -> bool:
    def lemonadeChange(self, bills):
        change = deque([])

        for bill in bills:
            if bill == 5:
                change.appendleft(5)

            else:
                if len(change) == 0:
                    return False

                elif bill == 10:
                    print(change)
                    change.popleft()
                    change.append(10)
                else:
                    print(change)
                    if min(change) != 5:
                        return False
                    if sum(change) < 15:
                        return False
                    if max(change) != 10:
                        change.popleft()
                        change.popleft()
                        change.popleft()
                    else:
                        change.popleft()
                        change.pop()

        return True


def main():
    sol = Solution()
    # bills = [5, 5, 5, 10, 20]
    # print(sol.lemonadeChange(bills))

    # bills = [5, 5, 10, 10, 20]
    # print(sol.lemonadeChange(bills))

    # bills = [10, 10]
    # print(sol.lemonadeChange(bills))

    # bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
    # print(sol.lemonadeChange(bills))

    bills = [5, 5, 5, 20, 5, 5, 5, 20, 5, 5,
             5, 10, 5, 20, 10, 20, 10, 20, 5, 5]
    print(sol.lemonadeChange(bills))

    pass


if __name__ == "__main__":
    main()
