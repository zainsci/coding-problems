#! /bin/python3

"""
source: https://leetcode.com/problems/maximum-number-of-pairs-in-array/
problem: https://leetcode.com/problems/maximum-number-of-pairs-in-array/
type: easy
site: LeetCode
"""


class Solution:
    # def numberOfPairs(self, nums: List[int]) -> List[int]:
    def numberOfPairs(self, nums):
        nums = sorted(nums)
        rem = [0, 0]

        while nums:
            try:
                if nums[0] == nums[1]:
                    nums.pop(0)
                    nums.pop(0)
                    rem[0] += 1

                else:
                    nums.pop(0)
                    rem[1] += 1
            except:
                nums.pop(0)
                rem[1] += 1

        return rem


def main():
    sol = Solution()

    nums = [1, 3, 2, 1, 3, 2, 2]
    print(sol.numberOfPairs(nums))

    nums = [1, 1]
    print(sol.numberOfPairs(nums))


if __name__ == "__main__":
    main()
