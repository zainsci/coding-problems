#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/truncate-sentence/
problem: https://leetcode.com/problems/truncate-sentence/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/truncate-sentence/submissions/1625521343/
"""


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])


def main():
    sol = Solution()

    s = "Hello how are you Contestant"
    k = 4
    print(sol.truncateSentence(s, k))

    s = "What is the solution to this problem"
    k = 4
    print(sol.truncateSentence(s, k))

    s = "chopper is not a tanuki"
    k = 5
    print(sol.truncateSentence(s, k))

    pass


if __name__ == "__main__":
    main()
