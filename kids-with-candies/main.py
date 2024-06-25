#! /bin/python3

"""
source: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
type: Easy
site: LeetCode
"""


class Solution:
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        out = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                out.append(True)
            else:
                out.append(False)

        return out


def main():
    sol = Solution()

    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(sol.kidsWithCandies(candies, extraCandies))

    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(sol.kidsWithCandies(candies, extraCandies))

    candies = [12, 1, 12]
    extraCandies = 10
    print(sol.kidsWithCandies(candies, extraCandies))

    return


if __name__ == "__main__":
    main()
