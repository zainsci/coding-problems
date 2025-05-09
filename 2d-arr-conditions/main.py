#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
problem: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/submissions/1629288282
"""


class Solution:
    # def findMatrix(self, nums: List[int]) -> List[List[int]]:
    def findMatrix(self, nums):
        ans = [[]]
        counter = {}
        counter_set = set()

        for i in nums:
            if i not in counter_set:
                counter_set.add(i)
                counter[i] = 0
                ans[0].append(i)

            else:
                counter[i] += 1
                if len(ans) <= counter[i]:
                    ans.append([])

                ans[counter[i]].append(i)

        return ans


def main():
    sol = Solution()

    nums = [1, 3, 4, 1, 2, 3, 1]
    print(sol.findMatrix(nums))

    nums = [1, 2, 3, 4]
    print(sol.findMatrix(nums))

    pass


if __name__ == "__main__":
    main()
