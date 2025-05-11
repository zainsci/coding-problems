#!/usr/bin/env python3
from collections import Counter

"""
source: https://leetcode.com/problems/count-elements-with-maximum-frequency/
problem: https://leetcode.com/problems/count-elements-with-maximum-frequency/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-elements-with-maximum-frequency/submissions/1631358409/
"""


class Solution:
    # def maxFrequencyElements(self, nums: List[int]) -> int:
    def maxFrequencyElements(self, nums):
        count = Counter(nums)
        ans = 0

        max_freq = max(count.values())

        for elem in count.keys():
            if count[elem] == max_freq:
                ans += max_freq

        return ans


def main():
    sol = Solution()

    nums = [1, 2, 2, 3, 1, 4]
    print(sol.maxFrequencyElements(nums))

    nums = [1, 2, 3, 4, 5]
    print(sol.maxFrequencyElements(nums))

    pass


if __name__ == "__main__":
    main()
