#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
problem: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/submissions/1627079287/
"""


class Solution:
    # def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
    def findThePrefixCommonArray(self, A, B):
        ans = []
        counter = {}

        for i in range(len(A)):
            curr_a = A[i]
            curr_b = B[i]

            if i == 0:
                if curr_a == curr_b:
                    ans.append(1)
                    counter[curr_a] = 2
                else:
                    ans.append(0)
                    counter[curr_a] = 1
                    counter[curr_b] = 1
                continue

            if curr_a not in counter.keys():
                counter[curr_a] = 1
            else:
                counter[curr_a] += 1

            if curr_b not in counter.keys():
                counter[curr_b] = 1
            else:
                counter[curr_b] += 1

            ans.append(sum([1 if x >= 2 else 0 for x in counter.values()]))

        return ans


def main():
    sol = Solution()

    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    print(sol.findThePrefixCommonArray(A, B))

    A = [2, 3, 1]
    B = [3, 1, 2]
    print(sol.findThePrefixCommonArray(A, B))

    A = [1, 2]
    B = [1, 2]
    print(sol.findThePrefixCommonArray(A, B))

    pass


if __name__ == "__main__":
    main()
