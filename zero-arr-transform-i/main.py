#!/usr/bin/env python3
from collections import Counter

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    def isZeroArray(self, nums, queries):

        def backtrack(start, path, src, res):
            res.append(path[:])

            for i in range(start, len(src)):
                path.append(src[i])
                backtrack(i+1, path, src, res)
                path.pop()

        for query in queries:
            subs = []
            backtrack(0, [], [x for x in range(query[0], query[1]+1)], subs)

            print(subs)

        return


def main():
    sol = Solution()

    nums = [1, 0, 1]
    queries = [[0, 2]]
    print(sol.isZeroArray(nums, queries))

    nums = [4, 3, 2, 1]
    queries = [[1, 3], [0, 2]]
    print(sol.isZeroArray(nums, queries))

    pass


if __name__ == "__main__":
    main()
