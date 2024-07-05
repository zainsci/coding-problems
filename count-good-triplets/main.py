#! /bin/python3

"""
source: https://leetcode.com/problems/count-good-triplets/
problem: https://leetcode.com/problems/count-good-triplets/
type: Easy
site: LeetCode
"""


class Solution:
    # def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    def countGoodTriplets(self, arr, a, b, c) -> int:
        good = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    x, y, z = arr[i], arr[j], arr[k]

                    if not (0 <= i < j < k < len(arr)):
                        continue
                    if not (abs(x - y) <= a):
                        continue
                    if not (abs(y - z) <= b):
                        continue
                    if not (abs(x - z) <= c):
                        continue

                    good += 1

        return good


def main():
    sol = Solution()

    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    print(sol.countGoodTriplets(arr, a, b, c))

    arr = [1, 1, 2, 2, 3]
    a = 0
    b = 0
    c = 1
    print(sol.countGoodTriplets(arr, a, b, c))

    return


if __name__ == "__main__":
    main()
