#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/reverse-integer/
problem: https://leetcode.com/problems/reverse-integer/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/reverse-integer/submissions/1627888235/
"""


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        bit_32 = 2**31

        if x < 0:
            num = -int(str(x)[1:][::-1])
        else:
            num = int(str(x)[::-1])

        return 0 if num < -bit_32 or num > (bit_32)-1 else num


def main():
    sol = Solution()

    x = 123
    print(sol.reverse(x))

    x = -123
    print(sol.reverse(x))

    x = 120
    print(sol.reverse(x))

    pass


if __name__ == "__main__":
    main()
