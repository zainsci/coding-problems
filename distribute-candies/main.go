package main

import (
	"fmt"
	"sort"
)

/*
 * source: https://leetcode.com/problems/distribute-candies/
 * problem: https://leetcode.com/problems/distribute-candies/
 * type: easy
 * site: LeetCode
 */

func distributeCandies(candyType []int) int {
	sort.Ints(candyType)
	total := 0
	for pos, num := range candyType {
		if pos == 0 {
			total += 1
		} else if num != candyType[pos-1] {
			total += 1
		}
	}

	if total > len(candyType)/2 {
		return len(candyType) / 2
	}
	return total
}

func main() {
	var candyType []int
	var sol int

	candyType = []int{1, 1, 2, 2, 3, 3}
	sol = distributeCandies(candyType[:])
	fmt.Println(sol)

	candyType = []int{1, 1, 2, 3}
	sol = distributeCandies(candyType[:])
	fmt.Println(sol)

	candyType = []int{6, 6, 6, 6}
	sol = distributeCandies(candyType[:])
	fmt.Println(sol)
}
