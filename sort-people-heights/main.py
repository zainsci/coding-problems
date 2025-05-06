#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sort-the-people/
problem: https://leetcode.com/problems/sort-the-people/
type: Easy  
site: LeetCode
submission: https://leetcode.com/problems/sort-the-people/submissions/1627302120/
"""


class Solution:
    # def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    def sortPeople(self, names, heights):
        people = [(names[x], heights[x]) for x in range(len(names))]

        return [x[0] for x in sorted(people, key=lambda x: x[1], reverse=True)]


def main():
    sol = Solution()

    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    print(sol.sortPeople(names, heights))

    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    print(sol.sortPeople(names, heights))

    pass


if __name__ == "__main__":
    main()
