package main

import "fmt"

/**
 * source: https://leetcode.com/problems/counting-bits/
 * problem: https://leetcode.com/problems/counting-bits/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/counting-bits/submissions/1645039017/
 */

func countBits(n int) []int {
	ans := []int{}

	for i := range n + 1 {
		count := 0

		for i != 0 {
			count += i & 1
			i >>= 1
		}

		ans = append(ans, count)
	}
	return ans
}

func main() {
	n := 2
	fmt.Println(countBits(n))

	n = 5
	fmt.Println(countBits(n))

}
