package main

import (
	"sort"
)

/**
 * source: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
 * problem: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/submissions/1642477815/
 */

func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	counter := make(map[int]int)
	ans := [][]int{}

	for idx := range nums1 {
		key, val := nums1[idx][0], nums1[idx][1]

		counter[key] = val
	}

	for idx := range nums2 {
		key, val := nums2[idx][0], nums2[idx][1]

		counter[key] += val
	}

	for key, val := range counter {
		temp := []int{key, val}
		ans = append(ans, temp)
	}

	sort.Slice(ans, func(i, j int) bool {
		return ans[i][0] < ans[j][0]
	})

	return ans
}

func main() {
	nums1 := [][]int{{1, 2}, {2, 3}, {4, 5}}
	nums2 := [][]int{{1, 4}, {3, 2}, {4, 1}}
	println(mergeArrays(nums1, nums2))

	nums1 = [][]int{{2, 4}, {3, 6}, {5, 5}}
	nums2 = [][]int{{1, 3}, {4, 3}}
	println(mergeArrays(nums1, nums2))

}
