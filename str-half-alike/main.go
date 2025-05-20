package main

import "unicode"

/**
 * source: https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/
 * problem: https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/determine-if-string-halves-are-alike/submissions/1639567279/
 */

func halvesAreAlike(s string) bool {
	vowels := map[string]bool{
		"a": true,
		"e": true,
		"i": true,
		"o": true,
		"u": true}

	half := len(s) / 2
	left := s[half:]
	right := s[:half]
	left_c := 0
	right_c := 0

	for i := range half {
		if vowels[string(unicode.ToLower(rune(left[i])))] {
			left_c++
		}

		if vowels[string(unicode.ToLower(rune(right[i])))] {
			right_c++
		}
	}

	return left_c == right_c
}

func main() {
	s := "book"
	println(halvesAreAlike(s))

	s = "textbook"
	println(halvesAreAlike(s))
}
