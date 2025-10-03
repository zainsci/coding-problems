#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-special-quadruplets/
problem: https://leetcode.com/problems/count-special-quadruplets/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-special-quadruplets/submissions/1790508920/
"""


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for c in range(2, n - 1):
            sum_map = {}

            for a in range(c):
                for b in range(a + 1, c):
                    ab = nums[a] + nums[b]
                    sum_map[ab] = sum_map.get(ab, 0) + 1

            for d in range(c + 1, n):
                target = nums[d] - nums[c]

                if target in sum_map:
                    count += sum_map[target]

        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
