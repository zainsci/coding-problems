#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/merge-similar-items/
problem: https://leetcode.com/problems/merge-similar-items/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/merge-similar-items/submissions/1633638690/
"""


class Solution:
    # def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    def mergeSimilarItems(self, items1, items2):
        ans = {}

        for x in items1:
            if x[0] in ans.keys():
                ans[x[0]] += x[1]
            else:
                ans[x[0]] = x[1]

        for x in items2:
            if x[0] in ans.keys():
                ans[x[0]] += x[1]
            else:
                ans[x[0]] = x[1]

        return sorted([[x, ans[x]] for x in ans.keys()], key=lambda x: x[0])


def main():
    sol = Solution()
    items1 = [[1, 1], [4, 5], [3, 8]]
    items2 = [[3, 1], [1, 5]]
    print(sol.mergeSimilarItems(items1, items2))

    items1 = [[1, 1], [3, 2], [2, 3]]
    items2 = [[2, 1], [3, 2], [1, 3]]
    print(sol.mergeSimilarItems(items1, items2))

    items1 = [[1, 3], [2, 2]]
    items2 = [[7, 1], [2, 2], [1, 4]]
    print(sol.mergeSimilarItems(items1, items2))

    pass


if __name__ == "__main__":
    main()
