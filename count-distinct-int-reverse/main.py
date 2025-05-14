#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
problem: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/submissions/1633972329/
"""


class Solution:
    # def countDistinctIntegers(self, nums: List[int]) -> int:
    def countDistinctIntegers(self, nums):
        nums = nums + [int(str(x)[::-1]) for x in nums]
        ans = set(nums)

        return len(ans)


def main():
    sol = Solution()

    nums = [1, 13, 10, 12, 31]
    print(sol.countDistinctIntegers(nums))

    nums = [2, 2, 2]
    print(sol.countDistinctIntegers(nums))

    pass


if __name__ == "__main__":
    main()
