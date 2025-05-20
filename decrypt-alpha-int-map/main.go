package main

import (
	"strconv"
	"strings"
)

/**
 * source: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
 * problem: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/1639438195/
 */

func freqAlphabets(s string) string {
	hash := make(map[string]string)
	for i := 106; i < 123; i++ {
		hash[strconv.Itoa(i-96)] = string(i)
	}

	ans := []string{}

	for i := range len(s) {
		char := s[i]
		if char == 35 {
			ans = ans[:len(ans)-2]
			ans = append(ans, string(hash[s[i-2:i]]))
		} else {
			ans = append(ans, string(s[i]+48))
		}
	}

	return strings.Join(ans, "")
}

func main() {
	s := "10#11#12"
	println(freqAlphabets(s))

	s = "1326#"
	println(freqAlphabets(s))

}
