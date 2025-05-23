package main

/**
 * source: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
 * problem: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/submissions/1642492795/
 */

import (
	"fmt"
	"sort"
)

func canBeEqual(target []int, arr []int) bool {
	sort.Ints(target)
	sort.Ints(arr)

	for i := range len(arr) {
		if target[i] != arr[i] {
			return false
		}
	}
	return true
}

func main() {

	target := []int{1, 2, 3, 4}
	arr := []int{2, 4, 1, 3}
	fmt.Println(canBeEqual(target, arr))

	target = []int{7}
	arr = []int{7}
	fmt.Println(canBeEqual(target, arr))

	target = []int{3, 7, 9}
	arr = []int{3, 7, 11}
	fmt.Println(canBeEqual(target, arr))
}
