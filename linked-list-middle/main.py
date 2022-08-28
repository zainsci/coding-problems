#! /bin/python3

"""
source: https://leetcode.com/problems/middle-of-the-linked-list
problem: https://leetcode.com/problems/middle-of-the-linked-list
type: easy
site: LeetCode
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def middleNode(self, head):
        i = 0
        temp = head

        while temp:
            i += 1
            temp = temp.next
        mid = i // 2

        for i in range(mid):
            head = head.next

        return head


def main():
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = sol.middleNode(head)
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print(None)

    head = ListNode(1, ListNode(2, ListNode(
        3, ListNode(4, ListNode(5, ListNode(6))))))
    new_head = sol.middleNode(head)
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
    print(None)


if __name__ == "__main__":
    main()
