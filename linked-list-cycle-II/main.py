#! /bin/python3

"""
source: https://leetcode.com/problems/linked-list-cycle-ii
problem: https://leetcode.com/problems/linked-list-cycle-ii
type: medium
site: LeetCode
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def detectCycle(self, head):
        arr = set()
        temp = head

        while temp:
            if temp in arr:
                return temp
            else:
                arr.add(temp)
            temp = temp.next

        return None


def main():
    sol = Solution()
    tmp1 = ListNode(-4)
    tmp2 = ListNode(0)
    tmp3 = ListNode(2)
    head = ListNode(3)

    head.next = tmp3
    tmp3.next = tmp2
    tmp2.next = tmp1
    tmp1.next = tmp3

    val = sol.detectCycle(head)
    print(val)

    tmp1 = ListNode(1)
    head = ListNode(2)
    tmp1.next = head
    head.next = tmp1

    val = sol.detectCycle(head)
    print(val)


if __name__ == "__main__":
    main()
