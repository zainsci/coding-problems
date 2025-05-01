#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/decode-xored-array/
problem: https://leetcode.com/problems/decode-xored-array/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/decode-xored-array/submissions/1623118207/
"""


class Solution:
    # def decode(self, encoded: List[int], first: int) -> List[int]:
    def decode(self, encoded, first):
        arr = [first]+encoded
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] ^ arr[i]

        return arr


def main():
    sol = Solution()

    encoded = [1, 2, 3]
    first = 1
    print(sol.decode(encoded, first))

    encoded = [6, 2, 7, 3]
    first = 4
    print(sol.decode(encoded, first))

    pass


if __name__ == "__main__":
    main()
