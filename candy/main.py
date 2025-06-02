#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/candy/
problem: https://leetcode.com/problems/candy/
type: Hard
site: LeetCode
submission: https://leetcode.com/problems/candy/submissions/1651932928/
"""


class Solution:
    # def candy(self, ratings: List[int]) -> int:
    def candy(self, ratings):
        candies = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1]+1

        return sum(candies)


def main():
    sol = Solution()

    ratings = [1, 0, 2]
    print(sol.candy(ratings))

    ratings = [1, 2, 2]
    print(sol.candy(ratings))

    pass


if __name__ == "__main__":
    main()
