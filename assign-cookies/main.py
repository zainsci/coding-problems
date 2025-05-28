#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/assign-cookies/
problem: https://leetcode.com/problems/assign-cookies/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/assign-cookies/submissions/1646904936/
"""


class Solution:
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    def findContentChildren(self, g, s):
        left, right, count = 0, 0, 0
        g, s = sorted(g), sorted(s)

        while right < len(s) and left < len(g):
            if g[left] <= s[right]:
                count += 1
                left += 1
                right += 1

            else:
                if g[left] > s[right]:
                    right += 1

        return count


def main():
    sol = Solution()

    g = [1, 2, 3]
    s = [1, 1]
    print(sol.findContentChildren(g, s))

    g = [1, 2]
    s = [1, 2, 3]
    print(sol.findContentChildren(g, s))

    pass


if __name__ == "__main__":
    main()
