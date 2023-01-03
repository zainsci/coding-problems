#! /bin/python3


"""
source: 
problem: 
type: easy
site: LeetCode
"""


class Solution:
    # def sumOfUnique(self, nums: List[int]) -> int:
    def sumOfUnique(self, nums):
        total = 0
        counts = {}

        for num in nums:
            if num not in counts.keys():
                counts[num] = 1
            else:
                counts[num] += 1
        for key, value in counts.items():
            if value == 1:
                total += key

        return total


def main():
    sol = Solution()
    nums = [1, 2, 3, 2]
    print(sol.sumOfUnique(nums))

    nums = [1, 1, 1, 1, 1]
    print(sol.sumOfUnique(nums))

    nums = [1, 2, 3, 4, 5]
    print(sol.sumOfUnique(nums))


if __name__ == "__main__":
    main()
