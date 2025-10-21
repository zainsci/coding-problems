#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-population-year/
problem: https://leetcode.com/problems/maximum-population-year/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-population-year/submissions/1807803438/
"""


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [year for years in logs for year in years]
        low, high = min(years), max(years)

        res = (low, 0)
        count = {x: 0 for x in range(low, high)}

        for year in range(low, high):
            for person in logs:
                if person[0] <= year and person[1] > year:
                    count[year] += 1

                    if res[1] < count[year]:
                        res = (year, count[year])

        return res[0]


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
