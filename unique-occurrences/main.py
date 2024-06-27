#! /bin/python3
from collections import Counter


"""
source: https://leetcode.com/problems/unique-number-of-occurrences/
problem: https://leetcode.com/problems/unique-number-of-occurrences/
type: Easy
site: LeetCode
"""


# Solution 01
# class Solution:
#     # def uniqueOccurrences(self, arr: List[int]) -> bool:
#     def uniqueOccurrences(self, arr):
#         arr_nums = Counter(arr)
#         arr_sorted = sorted(list(arr_nums.values()))

#         for i in range(1, len(arr_sorted)):
#             if arr_sorted[i] == arr_sorted[i-1]:
#                 return False

#         return True

# Solution 02
# class Solution:
#     # def uniqueOccurrences(self, arr: List[int]) -> bool:
#     def uniqueOccurrences(self, arr):
#         arr_nums = Counter(arr)
#         checked = set()

#         for num in arr_nums.values():
#             if num in checked:
#                 return False
#             else:
#                 checked.add(num)
#         return True


class Solution:
    # def uniqueOccurrences(self, arr: List[int]) -> bool:
    def uniqueOccurrences(self, arr):
        arr_count = Counter(arr)
        return len(arr_count) == len(set(arr_count.values()))


def main():
    sol = Solution()

    arr = [1, 2, 2, 1, 1, 3]
    print(sol.uniqueOccurrences(arr))

    arr = [1, 2]
    print(sol.uniqueOccurrences(arr))

    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(sol.uniqueOccurrences(arr))

    return


if __name__ == "__main__":
    main()
