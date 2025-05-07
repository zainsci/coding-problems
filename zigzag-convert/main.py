#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/zigzag-conversion/
problem: https://leetcode.com/problems/zigzag-conversion/
type: Medium
site: LeetCode
submission: 
"""

# TODO: WORKS FOR THE GIVEN EXAMPLES BUT FAILS ON EDGE CASES


class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    def convert(self, s, numRows):
        if len(s) == 1 or numRows == 1:
            return s

        if len(s) == numRows or numRows > len(s):
            return s

        if len(s) == 3 and numRows == 2:
            return s[0]+s[1:][::-1]

        seq = []
        seq_counter = 0

        while len(seq) < len(s)//2:
            idx = numRows - (seq_counter % numRows)

            if idx == 1:
                seq_counter += 1
                continue

            seq.append(idx)
            seq_counter += 1

        build = []
        n = 0

        for i in range(len(seq)):
            idx = seq[i]

            if idx == numRows:
                col = list(s[n:n+numRows])

                if len(col) < numRows:
                    col.extend([" " for x in range(numRows-len(col))])

                build.append(col)
                n += numRows
            else:
                col = [" " for x in range(idx-1)]
                col.append(s[n])

                for i in range(numRows-len(col)):
                    col.extend(" ")
                n += 1
                build.append(col)

        x, y = len(build), len(build[0])
        new_matrix = [[None for _ in range(x)] for _ in range(y)]

        for i in range(x):
            for j in range(y):
                new_matrix[j][i] = build[i][j]

        return "".join(["".join(x) for x in new_matrix]).replace(" ", "")


def main():
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows))

    s = "PAYPALISHIRING"
    numRows = 4
    print(sol.convert(s, numRows))

    s = "A"
    numRows = 1
    print(sol.convert(s, numRows))

    pass


if __name__ == "__main__":
    main()
