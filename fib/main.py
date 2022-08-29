#! /bin/python3

"""
intro to dynammic programming
source: https://www.youtube.com/watch?v=vYquumk4nWw
"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_memo(n, memo):
    if memo[n] is not None:
        return memo[n]

    if n == 1 or n == 2:
        memo[n] = 1
        return 1

    result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result

    return result


def main():
    print(fib(5))
    print(fib(20))
    print(fib(35))

    print(fib_memo(35, [None for _ in range(35+1)]))
    print(fib_memo(100, [None for _ in range(100+1)]))
    print(fib_memo(500, [None for _ in range(500+1)]))


if __name__ == "__main__":
    main()
