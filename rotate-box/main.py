#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/rotating-the-box/
problem: https://leetcode.com/problems/rotating-the-box/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/rotating-the-box/submissions/1665212749/
"""


class Solution:
    # def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
    def rotateTheBox(self, boxGrid):
        for i in range(len(boxGrid)):
            rows = "".join(boxGrid[i]).split("*")

            for j in range(len(rows)):
                row = list(rows[j])
                h = row.count("#")
                d = row.count(".")

                for k in range(d):
                    row[k] = "."
                for k in range(d, d+h):
                    row[k] = "#"
                rows[j] = "".join(row)

            boxGrid[i] = list("*".join(rows))

        res = [list(range(len(boxGrid))) for _ in range(len(boxGrid[0]))]
        for i in range(len(boxGrid)):
            y = len(res[0])
            for j in range(len(boxGrid[0])):
                res[j][y-i-1] = boxGrid[i][j]

        return res


def main():
    sol = Solution()
    boxGrid = [["#", ".", "#"]]
    print(sol.rotateTheBox(boxGrid))

    boxGrid = [["#", ".", "*", "."],
               ["#", "#", "*", "."]]
    print(sol.rotateTheBox(boxGrid))

    boxGrid = [["#", "#", "*", ".", "*", "."],
               ["#", "#", "#", "*", ".", "."],
               ["#", "#", "#", ".", "#", "."]]
    print(sol.rotateTheBox(boxGrid))

    boxGrid = [["*", "#", "*", ".", ".", ".", "#", ".", "*", "."]]
    print(sol.rotateTheBox(boxGrid))

    pass


if __name__ == "__main__":
    main()
