#! /bin/python3
# from collections import Counter

"""
source: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
problem: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
type: Easy
site: LeetCode
"""


# Works but Slow
# class Solution:
#     def minimumRecolors(self, blocks, k):
#         min_ops = 1000
#
#         for i in range(len(blocks)-k+1):
#             block_count = Counter(blocks[i:i+k])
#
#             if block_count["W"] < min_ops:
#                 min_ops = block_count["W"]
#
#         return min_ops


class Solution:
    # def minimumRecolors(self, blocks: str, k: int) -> int:
    def minimumRecolors(self, blocks, k):
        min_ops = 0
        ans = 0

        for i in range(k):
            if blocks[i] == "W":
                min_ops += 1
                ans = min_ops

        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                min_ops += 1
            if blocks[i-k] == "W":
                min_ops -= 1

            ans = min(ans, min_ops, )

        return ans


def main():
    sol = Solution()

    blocks = "WBBWWBBWBW"
    k = 7
    print(sol.minimumRecolors(blocks, k))

    blocks = "WBWBBBW"
    k = 2
    print(sol.minimumRecolors(blocks, k))

    return


if __name__ == "__main__":
    main()
