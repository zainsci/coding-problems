#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1648981664/
"""


class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target):

        for num in numbers:
            idx = numbers.index(num)
            sec = target-num

            if num == sec:
                return [idx+1, idx+2]

            if target-num in numbers:
                return [idx+1, numbers.index(target-num)+1]


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
