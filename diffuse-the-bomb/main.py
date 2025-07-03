#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/defuse-the-bomb/
problem: https://leetcode.com/problems/defuse-the-bomb/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/defuse-the-bomb/submissions/1684277652/
"""


class Solution:
    # def decrypt(self, code: List[int], k: int) -> List[int]:
    def decrypt(self, code, k):
        n = len(code)
        if k < 0:
            code = code[::-1]

        code = code + code[:abs(k)]
        out = []
        for i in range(1, n+1):
            out.append(sum(code[i:i+abs(k)]))

        if k < 0:
            return out[::-1]
        return out


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
