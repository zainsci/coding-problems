#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
problem: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/submissions/1672854951/
"""


class Solution:
    # def divideString(self, s: str, k: int, fill: str) -> List[str]:
    def divideString(self, s, k, fill):
        if not len(s) % k == 0:
            s = s + (k - len(s) % k)*fill
        return [s[x:x+k] for x in range(0, len(s), k)]


def main():
    sol = Solution()

    s = "abcdefghi"
    k = 3
    fill = "x"
    print(sol.divideString(s, k, fill))

    s = "abcdefghij"
    k = 3
    fill = "x"
    print(sol.divideString(s, k, fill))

    pass


if __name__ == "__main__":
    main()
