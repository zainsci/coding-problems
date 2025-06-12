#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/binary-tree-inorder-traversal/
problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1661805191/
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def inorderTraversal(self, root):
        out = []

        def traverse(node):
            if node:
                traverse(node.left)
                out.append(node.val)
                traverse(node.right)

        traverse(root)
        return out


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
