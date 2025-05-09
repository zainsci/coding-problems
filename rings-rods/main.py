#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/rings-and-rods/
problem: https://leetcode.com/problems/rings-and-rods/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/rings-and-rods/submissions/1629415648/
"""


class Solution:
    # def countPoints(self, rings: str) -> int:
    def countPoints(self, rings):
        counter = {}

        for seq in range(0, len(rings), 2):
            ring, rod = rings[seq], rings[seq+1]

            if rod in counter.keys():
                counter[rod].add(ring)
            else:
                counter[rod] = set(ring)

        return sum([1 for x in counter.keys() if len(counter[x]) == 3])


def main():
    sol = Solution()

    rings = "B0B6G0R6R0R6G9"
    print(sol.countPoints(rings))

    rings = "B0R0G0R9R0B0G0"
    print(sol.countPoints(rings))

    rings = "G4"
    print(sol.countPoints(rings))

    pass


if __name__ == "__main__":
    main()
