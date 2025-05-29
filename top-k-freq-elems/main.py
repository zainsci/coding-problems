#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/top-k-frequent-elements/
problem: https://leetcode.com/problems/top-k-frequent-elements/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/top-k-frequent-elements/submissions/1648006845/
"""


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        freq = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in freq][:k]


def main():
    sol = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(sol.topKFrequent(nums, k))

    nums = [1]
    k = 1
    print(sol.topKFrequent(nums, k))

    pass


if __name__ == "__main__":
    main()
