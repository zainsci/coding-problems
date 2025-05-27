package main

/**
 * source: https://leetcode.com/problems/subsets/
 * problem: https://leetcode.com/problems/subsets/
 * type: Medium
 * site: LeetCode
 * submission: https://leetcode.com/problems/subsets/submissions/1645913091/
 */

import (
	"fmt"
)

func subsets(nums []int) [][]int {
	subs := [][]int{}
	var backtrack func(start int, path []int)

	backtrack = func(start int, path []int) {
		tmp := make([]int, len(path))
		copy(tmp, path)
		subs = append(subs, tmp)

		for i := start; i < len(nums); i++ {
			path = append(path, nums[i])
			backtrack(i+1, path)
			path = path[:len(path)-1]
		}

	}

	backtrack(0, []int{})
	return subs
}

func main() {
	nums := []int{1, 2, 3}
	fmt.Println(subsets(nums))

	nums = []int{0}
	fmt.Println(subsets(nums))

}
