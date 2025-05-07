#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/shuffle-the-array/
problem: https://leetcode.com/problems/shuffle-the-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/shuffle-the-array/submissions/1627940186/
"""


class Solution:
    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])

        return ans


def main():
    sol = Solution()

    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(sol.shuffle(nums, n))

    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    print(sol.shuffle(nums, n))

    nums = [1, 1, 2, 2]
    n = 2
    print(sol.shuffle(nums, n))

    pass


if __name__ == "__main__":
    main()
