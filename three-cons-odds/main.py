#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/three-consecutive-odds/
problem: https://leetcode.com/problems/three-consecutive-odds/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/three-consecutive-odds/submissions/1631697142/
"""


class Solution:
    # def threeConsecutiveOdds(self, a: List[int]) -> bool:
    def threeConsecutiveOdds(self, arr):
        for i in range(2, len(arr)):
            if arr[i-2] % 2 and arr[i-1] % 2 and arr[i] % 2:
                return True

        return False


def main():
    sol = Solution()

    arr = [2, 6, 4, 1]
    print(sol.threeConsecutiveOdds(arr))

    arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(sol.threeConsecutiveOdds(arr))

    pass


if __name__ == "__main__":
    main()
