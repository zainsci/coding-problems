package main

/**
 * source: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
 * problem: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/submissions/1643330378/
 */

import (
	"fmt"
)

func minimumOperations(nums []int) int {
	sum := 0
	for _, x := range nums {
		if x%3 != 0 {
			sum++
		}
	}
	return sum
}

func main() {
	nums := []int{1, 2, 3, 4}
	fmt.Println(minimumOperations(nums))

	nums = []int{3, 6, 9}
	fmt.Println(minimumOperations(nums))

}
