#!/usr/bin/env python3
from collections import deque

"""
source: 
problem: 
type: 
site: 
submission: 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def searchBST(self, root, val):
        que = deque([root])

        while len(que) > 0:
            curr = que.popleft()

            if curr.val == val:
                return curr

            if curr:
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)

        return


def main():
    sol = Solution()

    print()
    pass


if __name__ == "__main__":
    main()
