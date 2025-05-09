#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-maximum-number-of-string-pairs/
problem: https://leetcode.com/problems/find-maximum-number-of-string-pairs/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/find-maximum-number-of-string-pairs/submissions/1629407888/
"""


class Solution:
    # def maximumNumberOfStringPairs(self, words: List[str]) -> int:
    def maximumNumberOfStringPairs(self, words):
        count = 0
        reverse_set = set()

        for word in words:
            if word not in reverse_set:
                reverse_set.add(word[::-1])
            else:
                count += 1

        return count


def main():
    sol = Solution()

    words = ["cd", "ac", "dc", "ca", "zz"]
    print(sol.maximumNumberOfStringPairs(words))

    words = ["ab", "ba", "cc"]
    print(sol.maximumNumberOfStringPairs(words))

    words = ["aa", "ab"]
    print(sol.maximumNumberOfStringPairs(words))

    pass


if __name__ == "__main__":
    main()
