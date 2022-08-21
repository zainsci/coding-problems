#! /bin/python3

"""
source: https://leetcode.com/problems/roman-to-integer
problem: https://leetcode.com/problems/roman-to-integer
site: LeetCode
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        number = 0
        i = 0

        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in roman:
                number += roman[s[i:i+2]]
                i += 2
            else:
                number += roman[s[i]]
                i += 1

        return number


def main():
    s = "IX"
    sol = Solution()
    solution = sol.romanToInt(s)
    print(solution)


if __name__ == "__main__":
    main()
