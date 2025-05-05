#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/shuffle-string/
problem: https://leetcode.com/problems/shuffle-string/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/shuffle-string/submissions/1626482347/
"""


class Solution:
    # def restoreString(self, s: str, indices: List[int]) -> str:
    def restoreString(self, s, indices):
        ans = list(s)
        for idx, val in enumerate(indices):
            ans[val] = s[idx]
        return "".join(ans)


def main():
    sol = Solution()

    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    print(sol.restoreString(s, indices))

    s = "abc"
    indices = [0, 1, 2]
    print(sol.restoreString(s, indices))
    pass


if __name__ == "__main__":
    main()
