#!/usr/bin/env python3
import sys

"""
source: https://codeforces.com/problemset/problem/1873/C
problem: https://codeforces.com/problemset/problem/1873/C
type: Easy
site: CodeForces
submission: https://codeforces.com/problemset/submission/1873/395454898
"""


i = \
"""XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX"""


"""
x: 0,9
y: 0-9 == 1

x: 1,8
y: 0,9 == 1
y: 1-8 == 2

x: 2,7
y: 0,9 == 1
y: 1,8 == 2
y: 2-7 == 3

x: 3,6
y: 0,9 == 1
y: 1,8 == 2
y: 2,7 == 3
y: 3-6 == 4

x: 4,5
y: 0,9 == 1
y: 1,8 == 2
y: 2,7 == 3
y: 3,6 == 4
y: 4-5 == 5
"""

grid = {
    0: {i: 1 for i in list(range(10))},
    1: {0: 1, 9: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2,},
    2: {0: 1, 9: 1, 1: 2, 8: 2, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3,},
    3: {0: 1, 9: 1, 1: 2, 8: 2, 2: 3, 7: 3, 3: 4, 4: 4, 5: 4, 6: 4,},
    4: {0: 1, 9: 1, 1: 2, 8: 2, 2: 3, 7: 3, 3: 4, 6: 4, 4: 5, 5: 5,},
    5: {0: 1, 9: 1, 1: 2, 8: 2, 2: 3, 7: 3, 3: 4, 6: 4, 4: 5, 5: 5,},
    6: {0: 1, 9: 1, 1: 2, 8: 2, 2: 3, 7: 3, 3: 4, 4: 4, 5: 4, 6: 4,},
    7: {0: 1, 9: 1, 1: 2, 8: 2, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3,},
    8: {0: 1, 9: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2,},
    9: {i: 1 for i in list(range(10))}
}

def count_points():
    i_data = sys.stdin.read().splitlines()
    if not i_data:
            return

    t = int(i_data[0].strip())
    line_idx = 1

    for _ in range(t):
        rows = i_data[line_idx:line_idx + 10]
        line_idx += 10
        count = 0

        for x, row in enumerate(rows):
            for y, col in enumerate(row):
                if row[y] == "X":
                    count += grid[x][y]

        print(count)


if __name__ == "__main__":
    count_points()
