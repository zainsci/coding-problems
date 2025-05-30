#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1648983872/
"""


class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers)-1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]
            elif total > target:
                right -= 1
            else:
                left += 1


def main():
    sol = Solution()

    numbers = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(numbers, target))

    numbers = [2, 3, 4]
    target = 6
    print(sol.twoSum(numbers, target))

    numbers = [-1, 0]
    target = -1
    print(sol.twoSum(numbers, target))

    pass


if __name__ == "__main__":
    main()
