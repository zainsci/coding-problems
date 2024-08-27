#! /bin/python3

"""
source: https://leetcode.com/problems/plus-one/
problem: https://leetcode.com/problems/plus-one/
type: Easy
site: LeetCode
"""


# Beats 82.52% on First Try, Yay!
# https://leetcode.com/problems/plus-one/submissions/1370551756/
class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        count = -1

        if len(digits) == 0:
            return [1]

        while True:
            digits[count] += 1
            if digits[count] > 9:
                digits[count] -= 10
                count -= 1
                if count < -len(digits):
                    digits = [0]+digits
                continue

            else:
                break

        return digits


def main():
    sol = Solution()

    digits = [1, 2, 3]
    print(sol.plusOne(digits))

    digits = [4, 3, 2, 1]
    print(sol.plusOne(digits))

    digits = [9]
    print(sol.plusOne(digits))

    return


if __name__ == "__main__":
    main()
