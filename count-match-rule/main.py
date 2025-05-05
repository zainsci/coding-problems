#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-items-matching-a-rule/
problem: https://leetcode.com/problems/count-items-matching-a-rule/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-items-matching-a-rule/submissions/1626498192/
"""


class Solution:
    # def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0

        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    count += 1

            if ruleKey == "color":
                if item[1] == ruleValue:
                    count += 1

            if ruleKey == "name":
                if item[2] == ruleValue:
                    count += 1

        return count


def main():
    sol = Solution()

    items = [["phone", "blue", "pixel"], ["computer",
                                          "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    print(sol.countMatches(items, ruleKey, ruleValue))

    items = [["phone", "blue", "pixel"], ["computer",
                                          "silver", "phone"], ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"
    print(sol.countMatches(items, ruleKey, ruleValue))

    pass


if __name__ == "__main__":
    main()
