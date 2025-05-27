package main

/**
 * source: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
 * problem: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/submissions/1645859280/
 */

import (
	"fmt"
)

func differenceOfSums(n int, m int) int {
	x, y := 0, 0

	for i := 0; i < n+1; i++ {
		if i%m == 0 {
			x += i
		} else {
			y += i
		}
	}
	return y - x
}

func main() {
	n := 10
	m := 3
	fmt.Println(differenceOfSums(n, m))

	n = 5
	m = 6
	fmt.Println(differenceOfSums(n, m))

	n = 5
	m = 1
	fmt.Println(differenceOfSums(n, m))
}
