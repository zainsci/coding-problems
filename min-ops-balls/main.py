#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
problem: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/submissions/1625538928/
"""


# TODO: NEED TO IMPROVE ON EFFICIENY

class Solution:
    # def minOperations(self, boxes: str) -> List[int]:
    def minOperations(self, boxes):
        boxes = list(boxes)
        ans = []

        for i in range(len(boxes)):
            count = 0

            for j in range(len(boxes)):
                if i == j:
                    continue

                if boxes[j] == "1":
                    count += abs(i-j)

            ans.append(count)
            count = 0

        return ans


def main():
    sol = Solution()

    boxes = "110"
    print(sol.minOperations(boxes))

    boxes = "001011"
    print(sol.minOperations(boxes))

    pass


if __name__ == "__main__":
    main()
