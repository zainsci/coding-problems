#! /bin/python3


"""
source: https://leetcode.com/problems/find-the-maximum-achievable-number/
problem: https://leetcode.com/problems/find-the-maximum-achievable-number/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-the-maximum-achievable-number/submissions/1380862733/
"""


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t + t


def main():
    sol = Solution()

    num = 4
    t = 1
    print(sol.theMaximumAchievableX(num, t))

    num = 3
    t = 2
    print(sol.theMaximumAchievableX(num, t))


if __name__ == "__main__":
    main()
