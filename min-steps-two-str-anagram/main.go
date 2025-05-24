package main

/**
 * source: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
 * problem: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
 * type: Medium
 * site: LeetCode
 * submission: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/submissions/1642857521/
 */

import (
	"fmt"
)

func minSteps(s string, t string) int {
	count_s := make(map[string]int)
	count_t := make(map[string]int)
	ans := 0

	for i := range len(s) {
		count_s[string(s[i])] += 1
	}

	for i := range len(t) {
		count_t[string(t[i])] += 1
	}

	for key, val := range count_t {
		if count_t[key] > count_s[key] {
			ans += val - count_s[key]
		}
	}

	return ans
}

func main() {
	s := "bab"
	t := "aba"
	fmt.Println(minSteps(s, t))

	s = "leetcode"
	t = "practice"
	fmt.Println(minSteps(s, t))

	s = "anagram"
	t = "mangaar"
	fmt.Println(minSteps(s, t))
}
