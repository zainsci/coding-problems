#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/create-target-array-in-the-given-order/
problem: https://leetcode.com/problems/create-target-array-in-the-given-order/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/create-target-array-in-the-given-order/submissions/1623951952/
"""


class Solution:
    # def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
    def createTargetArray(self, nums, index):
        ans = []

        for i in range(len(index)):
            idx = index[i]
            val = nums[i]

            if idx < len(ans):
                ans = ans[:idx] + [val] + ans[idx:]
            else:
                ans.append(val)

        return ans


def main():
    sol = Solution()
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(sol.createTargetArray(nums, index))

    nums = [1, 2, 3, 4, 0]
    index = [0, 1, 2, 3, 0]
    print(sol.createTargetArray(nums, index))

    nums = [1]
    index = [0]
    print(sol.createTargetArray(nums, index))


if __name__ == "__main__":
    main()
