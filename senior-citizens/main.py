#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-senior-citizens/
problem: https://leetcode.com/problems/number-of-senior-citizens/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-senior-citizens/submissions/1646849935/
"""


class Solution:
    # def countSeniors(self, details: List[str]) -> int:
    def countSeniors(self, details):
        return sum(1 if int(x[11:13]) > 60 else 0 for x in details)


def main():
    sol = Solution()

    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    print(sol.countSeniors(details))

    details = ["1313579440F2036", "2921522980M5644"]
    print(sol.countSeniors(details))

    pass


if __name__ == "__main__":
    main()
