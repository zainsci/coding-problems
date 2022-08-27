#! /bin/python3


"""
source: https://leetcode.com/problems/reverse-linked-list
problem: https://leetcode.com/problems/reverse-linked-list
type: easy
site: LeetCode
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(self, head):
        new_list = None

        while head:
            this_node = head
            head = head.next
            this_node.next = new_list
            new_list = this_node

        return new_list


def main():
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_list = sol.reverseList(head)

    while new_list:
        print(new_list.val)
        new_list = new_list.next


if __name__ == "__main__":
    main()
