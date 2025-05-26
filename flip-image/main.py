#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/flipping-an-image/
problem: https://leetcode.com/problems/flipping-an-image/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/flipping-an-image/submissions/1644769009/
"""


class Solution:
    # def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    def flipAndInvertImage(self, image):
        rev = [x[::-1] for x in image]
        return [[1 if x == 0 else 0 for x in y] for y in rev]


def main():
    sol = Solution()

    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(sol.flipAndInvertImage(image))

    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    print(sol.flipAndInvertImage(image))

    pass


if __name__ == "__main__":
    main()
