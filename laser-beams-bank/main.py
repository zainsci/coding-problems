#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
problem: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/submissions/1627763812/
"""


class Solution:
    # def numberOfBeams(self, bank: List[str]) -> int:
    def numberOfBeams(self, bank):
        count = 0
        last_sum = 0

        for i in range(len(bank)):
            this_sum = bank[i].count("1")

            if this_sum > 0:
                count += last_sum * this_sum
                last_sum = this_sum

        return count


def main():
    sol = Solution()
    bank = ["011001", "000000", "010100", "001000"]
    print(sol.numberOfBeams(bank))

    bank = ["000", "111", "000"]
    print(sol.numberOfBeams(bank))

    pass


if __name__ == "__main__":
    main()
