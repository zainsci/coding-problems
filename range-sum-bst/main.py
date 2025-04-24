#! /bin/python3

"""
source: https://leetcode.com/problems/range-sum-of-bst/
problem: https://leetcode.com/problems/range-sum-of-bst/
type: Easy
site: LeetCode
submission: https://leetcode.com/problems/range-sum-of-bst/submissions/1617002168/
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def rangeSumBST(self, root, low, high):
        total = 0

        if root.val <= high and root.val >= low:
            total += root.val
        if root.left:
            total += self.rangeSumBST(root.left, low, high)
        if root.right:
            total += self.rangeSumBST(root.right, low, high)

        return total


def main():
    a = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)),
                 TreeNode(15, None, TreeNode(18)))
    b = TreeNode(10, TreeNode(
        5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))
    ), TreeNode(15, TreeNode(13), TreeNode(18)))

    sol = Solution()
    print(sol.rangeSumBST(a, 7, 15))
    print(sol.rangeSumBST(b, 6, 10))
    return


if __name__ == "__main__":
    main()
