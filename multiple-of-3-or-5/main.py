#! /bin/python3

"""
source: https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
problem: https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
type: 6 kyu
site: CodeWars
"""


def solution(number):
    nums = []
    for i in range(number):
        if i % 3 == 0:
            nums.append(i)
        elif i % 5 == 0:
            nums.append(i)
    return sum(nums)


def main():
    number = 10
    sol = solution(number)
    print(sol)


if __name__ == "__main__":
    main()
