#! /bin/python3

"""
source: https://leetcode.com/problems/binary-tree-level-order-traversal/
problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
type: medium
site: LeetCode
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    def levelOrder(self, root):
        if not root:
            return []

        levels = []
        queue = [(root, 0)]

        # starting from the level 0 since
        # root level is zero
        current_level = 0
        current_level_nodes = []

        while queue:
            node, level = queue.pop(0)

            if not node:
                continue

            # if the level of the current node equals the
            # current_level then append the val of the
            # current node to the list of current node
            if level == current_level:
                current_level_nodes.append(node.val)

            # else add the list of current level nodes
            # to levels and change the current level to
            # the node level
            else:
                levels.append(current_level_nodes)
                current_level = level
                current_level_nodes = [node.val]

            # Whenever we append a child to the queue
            # we also increase its level since the child
            # node is always a level below the parent node
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))

        # at last we check if there remains some items
        # in current_level_nodes and append those to levels
        if current_level_nodes:
            levels.append(current_level_nodes)

        return levels


def main():
    sol = Solution()
    root = TreeNode(3,
                    left=TreeNode(9),
                    right=TreeNode(20,
                                   left=TreeNode(15),
                                   right=TreeNode(7)
                                   ))
    print(sol.levelOrder(root))

    root = TreeNode(1,
                    left=TreeNode(2,
                                  left=TreeNode(4)),
                    right=TreeNode(3,
                                   right=TreeNode(5)
                                   ))
    print(sol.levelOrder(root))


if __name__ == "__main__":
    main()
