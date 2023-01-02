#! /bin/python3

"""
source: https://leetcode.com/problems/height-checker/
problem: https://leetcode.com/problems/height-checker/
type: easy
site: LeetCode
"""


class Solution:
    # def heightChecker(self, heights: List[int]) -> int:
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count


def main():
    sol = Solution()
    heights = [1, 1, 4, 2, 1, 3]
    print(sol.heightChecker(heights))


if __name__ == "__main__":
    main()
