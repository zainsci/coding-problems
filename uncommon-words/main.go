package main

import (
	"fmt"
	"strings"
)

/*
 * source: https://leetcode.com/problems/uncommon-words-from-two-sentences/
 * problem: https://leetcode.com/problems/uncommon-words-from-two-sentences/
 * type: easy
 * site: LeetCode
 */

func uncommonFromSentences(s1 string, s2 string) []string {
	var newS1 []string
	var newS2 []string

	dict := map[string]int{}
	var unique []string

	newS1 = strings.Split(s1, " ")
	newS2 = strings.Split(s2, " ")

	for _, word := range newS1 {
		if _, exists := dict[word]; exists {
			dict[word] += 1
		} else {
			dict[word] = 1
		}
	}

	for _, word := range newS2 {
		if _, exists := dict[word]; exists {
			dict[word] += 1
		} else {
			dict[word] = 1
		}
	}

	for key, value := range dict {
		if value == 1 {
			unique = append(unique, key)
		}
	}

	return unique
}

func main() {
	s1 := "this apple is sweet"
	s2 := "this apple is sour"
	sol := uncommonFromSentences(s1, s2)
	fmt.Println(sol)
}
