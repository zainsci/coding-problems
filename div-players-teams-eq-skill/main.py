#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
problem: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/submissions/1692477909/
"""


class Solution:
    # def dividePlayers(self, skill: List[int]) -> int:
    def dividePlayers(self, skill):
        skill = sorted(skill)
        n = len(skill)
        count = 0
        last = skill[0] + skill[-1]

        for i in range(n//2):
            a, b = (skill[i], skill[n-i-1])
            if a + b != last:
                return -1

            count += a * b

        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
