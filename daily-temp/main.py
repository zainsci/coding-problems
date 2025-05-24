#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/daily-temperatures/description/
problem: https://leetcode.com/problems/daily-temperatures/description/
type: Medium
site: LeetCode
submission: 
"""

# BRUTE FORCE WORKS BUT TIME LIMIT EXCEEDS
# TODO: FIX TIME LIMIT ISSUE


class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    def dailyTemperatures(self, temperatures):
        ans = []

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    break

            if len(ans) <= i:
                ans.append(0)

        return ans+[0 for _ in range(len(temperatures)-len(ans))]


def main():
    sol = Solution()

    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures))

    temperatures = [30, 40, 50, 60]
    print(sol.dailyTemperatures(temperatures))

    temperatures = [30, 60, 90]
    print(sol.dailyTemperatures(temperatures))

    temperatures = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
    print(sol.dailyTemperatures(temperatures))

    pass


if __name__ == "__main__":
    main()
