#! /bin/python3

"""
source: https://leetcode.com/problems/merge-two-sorted-lists/
problem: https://leetcode.com/problems/merge-two-sorted-lists/
type: easy
site: LeetCode
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def mergeTwoLists(self, list1, list2):
        new_list = None
        head_node = None

        while list1 and list2:
            if not new_list:
                if list1.val < list2.val:
                    new_list = list1
                    list1 = list1.next
                else:
                    new_list = list2
                    list2 = list2.next
                head_node = new_list
            else:
                if list1.val < list2.val:
                    head_node.next = list1
                    head_node = head_node.next
                    list1 = list1.next
                else:
                    head_node.next = list2
                    head_node = head_node.next
                    list2 = list2.next

        if list1 and head_node:
            head_node.next = list1
        elif list2 and head_node:
            head_node.next = list2

        if new_list:
            return new_list
        elif list1:
            return list1
        elif list2:
            return list2


def main():
    sol = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    new_list = sol.mergeTwoLists(list1, list2)

    while new_list:
        print(new_list.val)
        new_list = new_list.next


if __name__ == "__main__":
    main()
