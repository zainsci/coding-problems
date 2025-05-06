#!/usr/bin/env python3
from collections import deque


"""
source: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
problem: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/submissions/1627318841/
"""


class Solution:
    # def minimumAverage(self, nums: List[int]) -> float:
    def minimumAverage(self, nums):
        nums = deque(sorted(nums))
        avg = []

        for i in range(len(nums)//2):
            x, y = nums.popleft(), nums.pop()
            avg.append((x+y)/2)

        return min(avg)


def main():
    sol = Solution()

    nums = [7, 8, 3, 4, 15, 13, 4, 1]
    print(sol.minimumAverage(nums))

    nums = [1, 9, 8, 3, 10, 5]
    print(sol.minimumAverage(nums))

    nums = [1, 2, 3, 7, 8, 9]
    print(sol.minimumAverage(nums))

    pass


if __name__ == "__main__":
    main()
