#! /bin/python3

"""
source: https://leetcode.com/problems/can-place-flowers/
problem: https://leetcode.com/problems/can-place-flowers/
type: Easy
site: LeetCode
"""


class Solution:
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    def canPlaceFlowers(self, flowerbed, n):
        bed = flowerbed
        count = 0

        if n == 0:
            return True

        if len(bed) == 1 and bed[0] == 0:
            return True

        if len(bed) == 1 and bed[0] != 0:
            return False
        if len(bed) == 2 and bed[0] != 0:
            return False

        if bed[0] == 0 and bed[1] == 0:
            bed[0] = 1
            count += 1

        for i in range(1, len(flowerbed)-1):
            if bed[i-1] == 0 and bed[i] == 0 and bed[i+1] == 0:
                bed[i] = 1
                count += 1

        if bed[len(bed)-2] == 0 and bed[len(bed)-1] == 0:
            bed[len(bed)-1] = 1
            count += 1

        if count >= n:
            return True
        else:
            return False


def main():
    sol = Solution()

    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(sol.canPlaceFlowers(flowerbed, n))

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    print(sol.canPlaceFlowers(flowerbed, n))

    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2
    print(sol.canPlaceFlowers(flowerbed, n))

    flowerbed = [0, 0, 1, 0, 1]
    n = 1
    print(sol.canPlaceFlowers(flowerbed, n))

    flowerbed = [1, 0, 0, 0, 1, 0, 0]
    n = 2
    print(sol.canPlaceFlowers(flowerbed, n))

    return


if __name__ == "__main__":
    main()
