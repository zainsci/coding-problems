#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
problem: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/submissions/1647893678/
"""


class Solution:
    # def minPartitions(self, n: str) -> int:
    def minPartitions(self, n):
        return max(int(x) for x in set(n))


def main():
    sol = Solution()
    n = "32"
    print(sol.minPartitions(n))

    n = "82734"
    print(sol.minPartitions(n))

    n = "27346209830709182346"
    print(sol.minPartitions(n))

    pass


if __name__ == "__main__":
    main()
