package main

/**
 * source: https://leetcode.com/problems/find-words-containing-character/
 * problem: https://leetcode.com/problems/find-words-containing-character/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/find-words-containing-character/submissions/1645871345/
 */

import (
	"fmt"
)

func findWordsContaining(words []string, x byte) []int {
	ans := []int{}

	for idx, word := range words {
		for _, letter := range word {
			if letter == rune(x) {
				ans = append(ans, idx)
				break
			}
		}

	}
	return ans
}

func main() {
	words := []string{"leet", "code"}
	x := "e"
	fmt.Println(findWordsContaining(words, byte(x[0])))

	words = []string{"abc", "bcd", "aaaa", "cbc"}
	x = "a"
	fmt.Println(findWordsContaining(words, byte(x[0])))

	words = []string{"abc", "bcd", "aaaa", "cbc"}
	x = "z"
	fmt.Println(findWordsContaining(words, byte(x[0])))

}
