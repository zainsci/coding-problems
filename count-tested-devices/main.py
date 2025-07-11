#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/count-tested-devices-after-test-operations/
problem: https://leetcode.com/problems/count-tested-devices-after-test-operations/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/count-tested-devices-after-test-operations/submissions/1694579218/
"""


class Solution:
    # def countTestedDevices(self, batteryPercentages: List[int]) -> int:
    def countTestedDevices(self, batteryPercentages):
        count = 0

        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                batteryPercentages = batteryPercentages[:i]+[
                    i-1 if i > 0 else 0 for i in batteryPercentages[i:]]
                count += 1

        return count


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
