#!/usr/bin/env python3

"""
source: https://codeforces.com/problemset/problem/1999/A
problem: https://codeforces.com/problemset/problem/1999/A
type: Easy
site: CodeForces
submission: https://codeforces.com/problemset/submission/1999/395399121
"""


def main():
    t = int(input())

    for _ in range(t):
        num = input()

        print(int(num[0])+int(num[1]))


if __name__ == "__main__":
    main()
