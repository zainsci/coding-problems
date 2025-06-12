#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/increasing-order-search-tree/
problem: https://leetcode.com/problems/increasing-order-search-tree/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/increasing-order-search-tree/submissions/1661799521/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def increasingBST(self, root):
        out = TreeNode(None)
        res = out

        def traverse(node):
            nonlocal res

            if not node:
                return

            traverse(node.left)
            res.right = TreeNode(node.val)
            res = res.right
            traverse(node.right)

        traverse(root)
        return out.right


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
