#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
problem: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/1654495912/
"""


class Solution:
    # def freqAlphabets(self, s: str) -> str:
    def freqAlphabets(self, s):
        a = {f"{x}": chr(x+96) for x in range(1, 10)}
        b = {f"{x}": chr(x+96) for x in range(10, 27)}
        ans = []

        for i in range(len(s)):
            letter = s[i]
            if letter == "#":
                key = s[i-2:i]
                ans.pop()
                ans.pop()
                ans.append(b[key])
            else:
                ans.append(a.get(letter))

        return "".join(ans)


def main():
    sol = Solution()

    s = "10#11#12"
    print(sol.freqAlphabets(s))

    s = "1326#"
    print(sol.freqAlphabets(s))

    pass


if __name__ == "__main__":
    main()
