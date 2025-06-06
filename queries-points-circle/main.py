#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
    def countPoints(self, points, queries):
        count = [0]*len(queries)
        for i, query in enumerate(queries):
            x1, y1, r = query

            for point in points:
                x2, y2 = point

                # if x1-r == x2-r and x1+r == x2+r:
                #     continue

                if x1-r <= x2 <= x1+r and y1-r <= y2 <= y1+r:
                    print(x1-r, x1+r, x2-r, x2+r)
                    print(query, point)
                    count[i] += 1

        return count


def main():
    sol = Solution()

    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    print(sol.countPoints(points, queries))

    # points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    # queries = [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]
    # print(sol.countPoints(points, queries))

    pass


if __name__ == "__main__":
    main()
