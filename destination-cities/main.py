#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/destination-city/
problem: https://leetcode.com/problems/destination-city/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/destination-city/submissions/1631349156/
"""


class Solution:
    # def destCity(self, paths: List[List[str]]) -> str:
    def destCity(self, paths):
        cities = {}

        for path in paths:
            cities[path[0]] = path[1]

        curr_city = list(cities.keys())[0]

        while True:
            if not cities[curr_city] in cities.keys():
                break

            curr_city = cities[curr_city]

        return cities[curr_city]


def main():
    sol = Solution()

    paths = [["London", "New York"], [
        "New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(sol.destCity(paths))

    paths = [["B", "C"], ["D", "B"], ["C", "A"]]
    print(sol.destCity(paths))

    paths = [["A", "Z"]]
    print(sol.destCity(paths))

    pass


if __name__ == "__main__":
    main()
