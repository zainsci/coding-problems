#!/usr/bin/env python3

"""
source: 
problem: 
type: 
site: 
submission: 
"""


class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    def letterCombinations(self, digits):
        if digits == "":
            return []

        ans = []
        key_pad = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        if len(digits) == 1:
            return key_pad[digits].split("")

        first = key_pad[digits[0]]
        seqs = [key_pad[x] for x in digits[1:]]
        combs = set()
        return


def main():
    sol = Solution()

    digits = "23"
    print(sol.letterCombinations(digits))

    digits = ""
    print(sol.letterCombinations(digits))

    digits = "2"
    print(sol.letterCombinations(digits))

    pass


if __name__ == "__main__":
    main()
