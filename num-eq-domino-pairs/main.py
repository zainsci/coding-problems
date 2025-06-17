#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
problem: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/number-of-equivalent-domino-pairs/submissions/1666951684/
"""


class Solution:
    # def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    def numEquivDominoPairs(self, dominoes):
        counter = {}
        count = 0

        for dom in dominoes:
            dom = tuple(sorted(dom))

            if dom in counter.keys():
                count += counter[dom]
                counter[dom] += 1
            else:
                counter[dom] = 1

        return count


def main():
    sol = Solution()

    dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
    print(sol.numEquivDominoPairs(dominoes))

    dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    print(sol.numEquivDominoPairs(dominoes))

    pass


if __name__ == "__main__":
    main()
