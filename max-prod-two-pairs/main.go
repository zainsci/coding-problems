package main

/**
 * source: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
 * problem: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/submissions/1645024488/
 */

import (
	"fmt"
	"sort"
)

func maxProductDifference(nums []int) int {
	sort.Ints(nums)
	return (nums[len(nums)-1] * nums[len(nums)-2]) - (nums[0] * nums[1])
}

func main() {
	nums := []int{5, 6, 2, 7, 4}
	fmt.Println(maxProductDifference(nums))

	nums = []int{4, 2, 5, 9, 7, 4, 8}
	fmt.Println(maxProductDifference(nums))

}
