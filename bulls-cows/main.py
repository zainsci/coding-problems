#! /bin/python3

"""
source: https://leetcode.com/problems/bulls-and-cows/
problem: https://leetcode.com/problems/bulls-and-cows/
type: medium
site: LeetCode
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        secret, guess = list(secret), list(guess)
        rem_sec, rem_gue = [], []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                rem_sec.append(secret[i])
                rem_gue.append(guess[i])

        for i in range(len(rem_sec)):
            if rem_sec[i] in rem_gue:
                cows += 1

                g_i = rem_gue.index(rem_sec[i])
                rem_gue[g_i] = None
                rem_sec[i] = None

        return f"{bulls}A{cows}B"


def main():
    sol = Solution()
    secret = "1807"
    guess = "7810"
    print(sol.getHint(secret, guess))

    secret = "1123"
    guess = "0111"
    print(sol.getHint(secret, guess))

    secret = "10101010"
    guess = "01010101"
    print(sol.getHint(secret, guess))

    secret = "01011010"
    guess = "01010101"
    print(sol.getHint(secret, guess))


if __name__ == "__main__":
    main()
