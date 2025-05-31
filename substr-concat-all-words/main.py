#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
problem: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
type: Hard
site: LeetCode
submission:
"""

# TODO: TIME LIMIT EXCEEDS, NEED TO IMPROVE


class Solution:
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    def findSubstring(self, s, words):
        strs = list(gen_substr(words))
        subs = {}
        for str in strs:
            letter = str[0]
            if letter in subs:
                subs[letter].append(str)
            else:
                subs[letter] = [str]

        init = set(x[0] for x in words)
        n = len(strs[0])
        ans = []

        for i, letter in enumerate(s):
            if letter in init:
                if n > len(s):
                    break

                for word in subs[letter]:
                    if word == s[i:i+n]:
                        ans.append(i)
        return ans


def gen_substr(words):
    def backtrack(rem, curr, res):
        if not rem:
            res.add(curr)
            return
        for i in range(len(rem)):
            next_rem = rem[:i]+rem[i+1:]
            backtrack(next_rem, curr + rem[i], res)

    res = set()
    backtrack(words, "", res)
    return res


def main():
    sol = Solution()

    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(sol.findSubstring(s, words))

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    print(sol.findSubstring(s, words))

    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    print(sol.findSubstring(s, words))

    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]
    print(sol.findSubstring(s, words))

    pass


if __name__ == "__main__":
    main()
