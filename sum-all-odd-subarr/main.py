#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
problem: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/1634012220/
"""

# TODO: SOLVE USING SLIDING WINDOW TECHNIQUE


class Solution:
    # def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    def sumOddLengthSubarrays(self, arr):
        total = 0

        for i in range(1, len(arr)+1, 2):
            for j in range(len(arr)):

                sub = arr[j:j+i]
                if len(sub) < i:
                    continue
                total += sum(sub)

        return total


def main():
    sol = Solution()

    arr = [1, 4, 2, 5, 3]
    print(sol.sumOddLengthSubarrays(arr))

    arr = [1, 2]
    print(sol.sumOddLengthSubarrays(arr))

    arr = [10, 11, 12]
    print(sol.sumOddLengthSubarrays(arr))

    pass


if __name__ == "__main__":
    main()
