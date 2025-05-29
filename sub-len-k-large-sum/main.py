#!/usr/bin/env python3
from collections import deque


"""
source: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
problem: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/submissions/1647822830/
"""


class Solution:
    # def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    def maxSubsequence(self, nums, k):
        arr = sorted(nums)[len(nums)-k:]
        idxs = {x: [] for x in arr}
        ans = []

        for num in nums:
            if num in arr:
                idxs[num].append(len(ans))
                ans.append(num)

        for i in range(len(ans)-k):
            n = idxs[min(ans)].pop()
            ans.pop(n)

        return ans


def main():
    sol = Solution()

    nums = [2, 1, 3, 3]
    k = 2
    print(sol.maxSubsequence(nums, k))

    nums = [-1, -2, 3, 4]
    k = 3
    print(sol.maxSubsequence(nums, k))

    nums = [3, 4, 3, 3]
    k = 2
    print(sol.maxSubsequence(nums, k))

    nums = [-16, -13, 8, 16, 35, -17, 30, -8, 34, -2, -29, -35, 15, 13, -30, -34, 6, 15, 28, -23, 34, 28, -24, 15, -17, 10, 31, 32, -3, -36, 19, 31, -5, -21, -33, -18, -23, -37, -15, 12, -28, -
            40, 1, 38, 38, -38, 33, -35, -28, -40, 4, -15, -29, -33, -18, -9, -29, 20, 1, 36, -8, 23, -34, 16, -7, 13, 39, 38, 7, -7, -10, 30, 9, 26, 27, -37, -18, -25, 14, -36, 23, 28, -15, 35, -9, 1]
    k = 8
    print(sol.maxSubsequence(nums, k))  # [35,34,38,38,36,39,38,35]

    pass


if __name__ == "__main__":
    main()
