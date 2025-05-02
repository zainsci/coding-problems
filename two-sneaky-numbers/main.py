#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
problem: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/submissions/1623936329/
"""


class Solution:
    # def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    def getSneakyNumbers(self, nums):
        ans = []
        count = {}

        for i in nums:
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1
                if count[i] == 2:
                    ans.append(i)
                    if len(ans) == 2:
                        break

        return ans


def main():
    sol = Solution()

    nums = [0, 1, 1, 0]
    print(sol.getSneakyNumbers(nums))

    nums = [0, 3, 2, 1, 3, 2]
    print(sol.getSneakyNumbers(nums))

    nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
    print(sol.getSneakyNumbers(nums))

    pass


if __name__ == "__main__":
    main()
