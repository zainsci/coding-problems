#!/usr/bin/env python3


"""
source: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
problem: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/submissions/1627061040/
"""


class Solution:
    # def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    def groupThePeople(self, groupSizes):
        groups = {}
        group_keys = set()

        for i in range(len(groupSizes)):
            curr_group = groupSizes[i]

            if curr_group not in group_keys:
                groups[curr_group] = [[i]]
                group_keys.add(curr_group)

            else:
                if len(groups[curr_group][-1]) == curr_group:
                    groups[curr_group].append([i])

                else:
                    groups[curr_group][-1].append(i)

        ans = []
        for i in groups.values():
            ans = ans + i

        return ans


def main():
    sol = Solution()

    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(sol.groupThePeople(groupSizes))

    groupSizes = [2, 1, 3, 3, 3, 2]
    print(sol.groupThePeople(groupSizes))

    groupSizes = [2, 2, 1, 1, 1, 1, 1, 1]
    print(sol.groupThePeople(groupSizes))

    pass


if __name__ == "__main__":
    main()
