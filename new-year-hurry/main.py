#!/usr/bin/env python3

"""
source: https://codeforces.com/problemset/problem/750/A
problem: https://codeforces.com/problemset/problem/750/A
type: Easy
site: CodeForces
submission: https://codeforces.com/problemset/submission/750/398908827
"""

def sol(i):
    x, y = i.split()
    x, y = int(x), int(y)

    rem_time = (60*4) - y
    count = 0

    for j in range(x):
        curr = (j+1) * 5

        if curr > rem_time:
            break

        else:
            rem_time -= curr
            count += 1

    print(count)




if __name__ == "__main__":
    s = "3 222"
    sol(s)
    s = "4 190"
    sol(s)
    s = "7 1"
    sol(s)
