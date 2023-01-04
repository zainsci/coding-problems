package main

import (
	"fmt"
	"strconv"
)

/*
 * source: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 * problem: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
 * type: easy
 * site: LeetCode
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func getDecimalValue(head *ListNode) int {
	bin := fmt.Sprintf("%d", head.Val)
	var returnNum int64

	for head.Next != nil {
		head = head.Next
		bin = bin + fmt.Sprintf("%d", head.Val)
	}

	returnNum, _ = strconv.ParseInt(bin, 2, 64)

	return int(returnNum)
}

func main() {
	head := ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 0,
			Next: &ListNode{
				Val: 1,
			},
		},
	}
	sol := getDecimalValue(&head)
	fmt.Println(sol)
}
