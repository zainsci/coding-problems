#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def jump(self, nums: List[int]) -> int:
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 1

        count = 1
        total = 0
        i = 0

        while total <= n-1:
            cur = nums[i]
            print(cur, n)
            if cur >= n-1:
                break
            nex = nums[cur]

            for i in range(cur):
                nex = max(nex, nums[cur-i])

            total += cur + nex
            count += 1
            i += 1

        return count


def main():
    sol = Solution()

    # nums = [2, 3, 1, 1, 4]
    # print(sol.jump(nums))

    # nums = [2, 3, 0, 1, 4]
    # print(sol.jump(nums))

    # nums = [0]  # 0
    # print(sol.jump(nums))

    # nums = [1]  # 0
    # print(sol.jump(nums))

    # nums = [1, 2]
    # print(sol.jump(nums))

    # nums = [4, 1, 1, 3, 1, 1, 1]
    # print(sol.jump(nums))

    nums = [2, 3, 1]
    print(sol.jump(nums))

    pass


if __name__ == "__main__":
    main()
