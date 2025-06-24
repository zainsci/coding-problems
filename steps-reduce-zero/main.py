#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/1675377716/
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num > 0:
            if num & 1 == 1:
                num -= 1
                count += 1
            else:
                num = num // 2
                count += 1

        return count


def main():
    sol = Solution()

    num = 14
    print(sol.numberOfSteps(num))

    num = 8
    print(sol.numberOfSteps(num))

    pass


if __name__ == "__main__":
    main()
