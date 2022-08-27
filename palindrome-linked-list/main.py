#! /bin/python3

"""
source: https://leetcode.com/problems/palindrome-linked-list/
problem: https://leetcode.com/problems/palindrome-linked-list/
type: easy
site: LeetCode
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def isPalindrome(self, head):
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:] if len(arr) % 2 == 0 else arr[mid+1:]

        if left == right[::-1]:
            return True

        return False


def main():
    sol = Solution()

    head = ListNode(1, ListNode(2, ListNode(
        3, ListNode(4, ListNode(3, ListNode(2, ListNode(2)))))))
    print(sol.isPalindrome(head))

    head = ListNode(1, ListNode(2, ListNode(
        2, ListNode(1))))
    print(sol.isPalindrome(head))

    head = ListNode(1, ListNode(2, ListNode(
        3, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))))
    print(sol.isPalindrome(head))


if __name__ == "__main__":
    main()
