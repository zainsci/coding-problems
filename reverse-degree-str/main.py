#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/reverse-degree-of-a-string/description/
problem: https://leetcode.com/problems/reverse-degree-of-a-string/description/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/reverse-degree-of-a-string/submissions/1623880816/
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        idxs = {key: 26 - val for val,
                key in enumerate(
                    [chr(96+i) for i in range(1, 27)]
                )}

        total = 0
        for x, y in enumerate(s):

            total += idxs[y] * (x+1)

        return total


def main():
    sol = Solution()

    s = "abc"
    print(sol.reverseDegree(s))

    s = "zaza"
    print(sol.reverseDegree(s))
    pass


if __name__ == "__main__":
    main()
