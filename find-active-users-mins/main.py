#!/usr/bin/env python3
from collections import defaultdict

"""
source: https://leetcode.com/problems/finding-the-users-active-minutes/
problem: https://leetcode.com/problems/finding-the-users-active-minutes/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/finding-the-users-active-minutes/submissions/1633967485/
"""


class Solution:
    # def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
    def findingUsersActiveMinutes(self, logs, k):
        ans = [0 for _ in range(k)]
        ans_dict = defaultdict(set)

        for x in logs:
            id, log = x[0], x[1]
            ans_dict[id].add(log)

        for key in ans_dict.keys():
            l = len(ans_dict[key])
            ans[l-1] += 1

        return ans


def main():
    sol = Solution()

    logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    k = 5
    print(sol.findingUsersActiveMinutes(logs, k))

    logs = [[1, 1], [2, 2], [2, 3]]
    k = 4
    print(sol.findingUsersActiveMinutes(logs, k))

    pass


if __name__ == "__main__":
    main()
