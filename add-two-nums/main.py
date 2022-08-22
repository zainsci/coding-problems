#! /bin/python3

"""
source: https://leetcode.com/problems/add-two-numbers/
problem: https://leetcode.com/problems/add-two-numbers/
site: LeetCode
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_node = l1
        l2_node = l2
        rem = 0
        results = None
        last_node = None

        while True:
            if not l1_node and not l2_node:
                break
            add = 0
            add += l1_node.val if l1_node else 0
            add += l2_node.val if l2_node else 0
            add += rem
            rem = 0

            if add > 9:
                rem = int(str(add)[0])
                add = int(str(add)[1])

            if not results:
                results = ListNode(add)
                last_node = results
            else:
                new_node = ListNode(add)
                last_node.next = new_node
                last_node = new_node

            l1_node = l1_node.next if l1_node else l1_node
            l2_node = l2_node.next if l2_node else l2_node

        if rem > 0:
            new_node = ListNode(rem)
            last_node.next = new_node
            last_node = new_node

        return results


def print_list(l):
    print("[", end="")
    while l:
        print(f"{l.val}, ", end="")
        l = l.next
    print("]")


def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    results = Solution().addTwoNumbers(l1, l2)
    print_list(results)


if __name__ == "__main__":
    main()
