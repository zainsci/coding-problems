#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
problem: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/minimum-distance-between-bst-nodes/submissions/1671507971/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    def minDiffInBST(self, root):
        last = None
        diff = float("inf")

        def tra(node):
            if not node:
                return

            nonlocal last
            nonlocal diff

            tra(node.left)
            if last is not None:
                diff = min(diff, node.val - last)
            last = node.val
            tra(node.right)

        tra(root)

        return diff


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
