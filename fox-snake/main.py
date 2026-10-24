#!/usr/bin/env python3

"""
source: https://codeforces.com/problemset/problem/510/A
problem: https://codeforces.com/problemset/problem/510/A
type: Easy
site: CodeForces
submission: https://codeforces.com/problemset/submission/510/395872339
"""


def sol():
    n = 9
    z = 10
    idx = 0
    res = ""

    for x in range(n):
        curr = ""

        if x % 2 == 0:
            curr += "#"*z
        else:
            curr += "."*z

            curr = curr[:-1] + "#" if idx % 2 == 0 else "#" + curr[1:]
            idx += 1

        curr += "\n"
        res += curr

    print(res)

if __name__ == "__main__":
    sol()
