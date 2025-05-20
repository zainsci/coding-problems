package main

/**
 * source: https://leetcode.com/problems/reverse-string/
 * problem: https://leetcode.com/problems/reverse-string/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/reverse-string/submissions/1639448690/
 */

func reverseString(s []byte) {
	n := len(s) / 2

	for i := range n {
		temp := s[i]
		s[i] = s[len(s)-i-1]
		s[len(s)-i-1] = temp
	}
}

func main() {
	s := []string{"h", "e", "l", "l", "o"}
	s = []string{"H", "a", "n", "n", "a", "h"}

}
