package main

/**
 * source: https://leetcode.com/problems/minimum-number-game/
 * problem: https://leetcode.com/problems/minimum-number-game/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/minimum-number-game/submissions/1645325823/
 */

import (
	"fmt"
	"sort"
)

func numberGame(nums []int) []int {
	ans := []int{}
	sort.Ints(nums)

	for i := range len(nums) / 2 {
		ans = append(ans, nums[(2*i)+1])
		ans = append(ans, nums[(2*i)])
	}

	return ans
}

func main() {
	nums := []int{5, 4, 2, 3}
	fmt.Println(numberGame(nums))

	nums = []int{2, 5}
	fmt.Println(numberGame(nums))
}
