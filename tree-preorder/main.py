#! /bin/python3


"""
source: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
problem: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
type: easy
site: LeetCode
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # def preorder(self, root: 'Node') -> List[int]:
    def preorder(self, root):
        if not root:
            return []

        arr = [root.val]

        if not root.children:
            return arr
        else:
            for i in root.children:
                a = self.preorder(i)
                arr.extend(a)

            return arr


def main():
    sol = Solution()
    root = Node(1, [
                Node(3, [Node(5), Node(6)]),
                Node(2),
                Node(4)
                ])
    print(sol.preorder(root))

    root = Node(1, [
        Node(2),
        Node(3, [
            Node(6),
            Node(7, [Node(11, [Node(14)])])
        ]),
        Node(4, [
            Node(8, [Node(12)])
        ]),
        Node(5, [
            Node(9, [Node(13)]), Node(10)
        ]),
    ])
    print(sol.preorder(root))


if __name__ == "__main__":
    main()
