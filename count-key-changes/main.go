package main

/**
 * source: https://leetcode.com/problems/number-of-changing-keys/
 * problem: https://leetcode.com/problems/number-of-changing-keys/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/number-of-changing-keys/submissions/1639546026/
 */

func countKeyChanges(s string) int {
	if len(s) == 0 {
		return 0
	}

	count := 0

	for i := 1; i < len(s); i++ {
		if s[i-1] == s[i]+32 || s[i-1]+32 == s[i] || s[i-1] == s[i] {
			continue
		} else {
			count++
		}
	}

	return count
}

func main() {
	s := "aAbBcC"
	println(countKeyChanges(s))

	s = "AaAaAaaA"
	println(countKeyChanges(s))
}
