#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
problem: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/submissions/1628849326/
"""


class Solution:
    # def cellsInRange(self, s: str) -> List[str]:
    def cellsInRange(self, s):
        ans = []

        first, second = s.split(":")
        a1, a2 = first[0], first[1]
        b1, b2 = second[0], second[1]

        for letter in range(ord(a1), ord(b1)+1):
            char = chr(letter)
            for i in range(int(a2), int(b2)+1):
                ans.append(char+str(i))

        return ans


def main():
    sol = Solution()

    s = "K1:L2"
    print(sol.cellsInRange(s))

    s = "A1:F1"
    print(sol.cellsInRange(s))

    pass


if __name__ == "__main__":
    main()
