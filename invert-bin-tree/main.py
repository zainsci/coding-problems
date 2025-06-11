#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/invert-binary-tree/
problem: https://leetcode.com/problems/invert-binary-tree/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/invert-binary-tree/submissions/1660791316/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def invertTree(self, root):
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


def main():
    sol = Solution()
    print()
    pass


if __name__ == "__main__":
    main()
