#! /bin/python3

"""
source: https://leetcode.com/problems/container-with-most-water/
problem: https://leetcode.com/problems/container-with-most-water/
type: hard
site: LeetCode
"""


# Time Limit Exceeded :skull:
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         water = []
#         mid = len(height)//2
#         print(mid)
#         for i in range(len(height)):
#             for j in range(len(height)):
#                 dis = j - i
#                 area = height[i] * dis \
#                     if height[i] < height[j] \
#                     else height[j] * dis
#                 water.append(area)
#         return max(water)

class Solution:
    # def maxArea(self, height: List[int]) -> int:
    def maxArea(self, height):
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            dis = right - left
            area = 0

            if height[left] <= height[right]:
                area = height[left] * dis
                left += 1
            else:
                area = height[right] * dis
                right -= 1

            if maxarea < area:
                maxarea = area

        return maxarea


def main():
    sol = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 2, 1]
    height = [1, 0, 0, 0, 0, 0, 0, 2, 2]
    height = [2, 3, 4, 5, 18, 17, 6]
    height = [1, 1000, 1000, 6, 2, 5, 4, 8, 3, 7]
    print(sol.maxArea(height))


if __name__ == "__main__":
    main()
