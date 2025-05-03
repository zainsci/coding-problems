#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def decompressRLElist(self, nums: List[int]) -> List[int]:
    def decompressRLElist(self, nums):
        ans = []
        for i in range(0, len(nums), 2):
            fre, val = nums[i], nums[i+1]
            ans = ans + [val for _ in range(fre)]

        return ans


def main():
    sol = Solution()

    nums = [1, 2, 3, 4]
    print(sol.decompressRLElist(nums))

    nums = [1, 1, 2, 3]
    print(sol.decompressRLElist(nums))

    pass


if __name__ == "__main__":
    main()
