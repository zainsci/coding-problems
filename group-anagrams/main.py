#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/group-anagrams/
problem: https://leetcode.com/problems/group-anagrams/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/group-anagrams/submissions/1647998840/
"""


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        counter = {}
        counter_set = set([])

        for word in strs:
            w = "".join(sorted(word))
            if w in counter_set:
                counter[w].append(word)
            else:
                counter[w] = [word]
                counter_set.add(w)

        return list(counter.values())


def main():
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))

    strs = [""]
    print(sol.groupAnagrams(strs))

    strs = ["a"]
    print(sol.groupAnagrams(strs))

    pass


if __name__ == "__main__":
    main()
