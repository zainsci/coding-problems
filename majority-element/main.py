#! /bin/python3


"""
source: https://leetcode.com/problems/majority-element/
problem: https://leetcode.com/problems/majority-element/
type: Easy
site: LeetCode
"""


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        e = nums[0]
        c = {}
        for n in nums:
            if n in c.keys():
                c[n] += 1
                if max(c.values()) <= c[n]:
                    e = n
            else:
                c[n] = 1
        return e


def main():
    sol = Solution()

    nums = [3, 2, 3]
    print(sol.majorityElement(nums))

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(sol.majorityElement(nums))

    nums = [6, 5, 5]
    print(sol.majorityElement(nums))

    return


if __name__ == "__main__":
    main()
