#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
problem: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/submissions/1670625016/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def reverseOddLevels(self, root):
        def tra(left, right, level):
            if not left or not right:
                return

            if level & 1 == 1:
                left.val, right.val = right.val, left.val

            tra(left.left, right.right, level+1)
            tra(left.right, right.left, level+1)

        tra(root.left, root.right, 1)

        return root


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
