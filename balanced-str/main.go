package main

/**
 * source: https://leetcode.com/problems/check-balanced-string/
 * problem: https://leetcode.com/problems/check-balanced-string/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/check-balanced-string/submissions/1639404393/
 */

import (
	"strconv"
)

func isBalanced(num string) bool {
	n1 := 0
	n2 := 0

	for i := 0; i < len(num); i = i + 2 {
		n, _ := strconv.Atoi(string(num[i]))
		n1 = n1 + n
	}
	for i := 1; i < len(num); i = i + 2 {
		n, _ := strconv.Atoi(string(num[i]))
		n2 = n2 + n

	}

	return n1 == n2
}

func main() {
	num := "1234"
	println(isBalanced(num))

	num = "24123"
	println(isBalanced(num))

}
