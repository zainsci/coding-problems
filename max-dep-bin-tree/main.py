#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/maximum-depth-of-binary-tree/
problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/maximum-depth-of-binary-tree/solutions/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    def maxDepth(self, root):
        dep = 0

        def tra(node, level):
            nonlocal dep
            if not node:
                return

            dep = max(dep, level)
            tra(node.left, level+1)
            tra(node.right, level+1)
        tra(root, 1)

        return dep


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
