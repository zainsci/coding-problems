#! /bin/python3


"""
source: https://leetcode.com/problems/power-of-four/
problem: https://leetcode.com/problems/power-of-four/
type: easy
site: LeetCode
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False

        while n != 1:
            if n % 4 != 0:
                return False
            else:
                n = n // 4

        return True


def main():
    sol = Solution()
    print(sol.isPowerOfFour(16))
    print(sol.isPowerOfFour(5))
    print(sol.isPowerOfFour(0))
    print(sol.isPowerOfFour(1))
    print(sol.isPowerOfFour(2))
    print(sol.isPowerOfFour(3))
    print(sol.isPowerOfFour(8))
    print(sol.isPowerOfFour(9))
    print(sol.isPowerOfFour(64))


if __name__ == '__main__':
    main()
