package main

import (
	"fmt"
	"sort"
)

/*
 * source: https://leetcode.com/problems/contains-duplicate/
 * problem: https://leetcode.com/problems/contains-duplicate/
 * type: easy
 * site: LeetCode
 */

func containsDuplicate(nums []int) bool {
	sort.Ints(nums)

	for pos, val := range nums {
		if pos+1 < len(nums) {
			if val == nums[pos+1] {
				return true
			}
		}
	}

	return false
}

func main() {
	nums := []int{1, 2, 3, 1}
	sol := containsDuplicate(nums)
	fmt.Println(sol)
}
