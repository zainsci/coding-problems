#! /bin/python3

"""
source: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
problem: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
type: Medium
site: LeetCode
"""


# LeetCode: Time Limit Exceeded
# class Solution:
#     def maxVowels(self, s, k):
#         VOWELS = {"a", "e", "i", "o", "u"}
#         max_len = 0
#
#         for i in range(len(s)-k+1):
#             count = [1 if x in VOWELS else 0 for x in s[i:i+k]]
#
#             if sum(count) > max_len:
#                 max_len = sum(count)
#
#         return max_len


# https://stackoverflow.com/questions/8269916/what-is-sliding-window-algorithm-examples
# learned about Sliding Window Approach
class Solution:
    def maxVowels(self, s, k):
        VOWELS = {"a", "e", "i", "o", "u"}
        curr_sum = 0
        max_len = 0

        for i in range(k):
            curr_sum += 1 if s[i] in VOWELS else 0
            max_len = curr_sum

        for i in range(k, len(s)):
            if s[i] in VOWELS:
                curr_sum += 1
            if s[i-k] in VOWELS:
                curr_sum -= 1

            max_len = max(max_len, curr_sum)

        return max_len


def main():
    sol = Solution()

    s = "abciiidef"
    k = 3
    print(sol.maxVowels(s, k))

    s = "aeiou"
    k = 2
    print(sol.maxVowels(s, k))

    s = "leetcode"
    k = 3
    print(sol.maxVowels(s, k))

    s = "weallloveyou"
    k = 7
    print(sol.maxVowels(s, k))

    return


if __name__ == "__main__":
    main()
