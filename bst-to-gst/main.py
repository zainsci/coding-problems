#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
problem: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/submissions/1669613896/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def bstToGst(self, root):
        global last
        last = 0

        def up(node):
            global last
            if not node:
                return

            up(node.right)
            node.val = node.val + last
            last = node.val
            up(node.left)

        up(root)

        return root


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
