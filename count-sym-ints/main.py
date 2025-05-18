#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-symmetric-integers/
problem: https://leetcode.com/problems/count-symmetric-integers/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-symmetric-integers/submissions/1637458049/
"""


class Solution:
    # def countSymmetricIntegers(self, low: int, high: int) -> int:
    def countSymmetricIntegers(self, low, high):
        count = 0

        for i in range(low, high+1):
            num = str(i)
            n = len(num)

            if n % 2 == 0:
                left, right = num[n//2:], num[:n//2]
                if sum(int(x) for x in left) == sum(int(x) for x in right):
                    count += 1

        return count


def main():
    sol = Solution()

    low = 1
    high = 100
    print(sol.countSymmetricIntegers(low, high))

    low = 1200
    high = 1230
    print(sol.countSymmetricIntegers(low, high))

    pass


if __name__ == "__main__":
    main()
