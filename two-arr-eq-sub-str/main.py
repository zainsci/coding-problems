#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
problem: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/submissions/1642485362/
"""


class Solution:
    # def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    def canBeEqual(self, target, arr):
        target = sorted(target)
        arr = sorted(arr)

        for i in range(len(arr)):
            if target[i] != arr[i]:
                return False

        return True


def main():
    sol = Solution()

    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(sol.canBeEqual(target, arr))

    target = [7]
    arr = [7]
    print(sol.canBeEqual(target, arr))

    target = [3, 7, 9]
    arr = [3, 7, 11]
    print(sol.canBeEqual(target, arr))

    pass


if __name__ == "__main__":
    main()
