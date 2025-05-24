package main

/**
 * source: https://leetcode.com/problems/intersection-of-two-arrays/
 * problem: https://leetcode.com/problems/intersection-of-two-arrays/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/intersection-of-two-arrays/submissions/1642841285/
 */

func intersection(nums1 []int, nums2 []int) []int {
	counter := make(map[int]int)
	ans := []int{}

	for _, item := range nums1 {
		counter[item] = 1
	}

	for _, item := range nums2 {
		if counter[item] == 1 {
			counter[item] = 2
		}
	}

	for key, val := range counter {
		if val == 2 {
			ans = append(ans, key)
		}
	}

	return ans
}

func main() {
	nums1 := []int{1, 2, 2, 1}
	nums2 := []int{2, 2}
	print(intersection(nums1, nums2))

	nums1 = []int{4, 9, 5}
	nums2 = []int{9, 4, 9, 8, 4}
	print(intersection(nums1, nums2))

}
