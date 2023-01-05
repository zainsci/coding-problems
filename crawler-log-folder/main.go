package main

import "fmt"

/*
 * source: https://leetcode.com/problems/crawler-log-folder/
 * problem: https://leetcode.com/problems/crawler-log-folder/
 * type: easy
 * site: LeetCode
 */

func minOperations(logs []string) int {
	var steps int

	for i := 0; i < len(logs); i++ {
		if logs[i] == "./" {
			continue
		} else {
			if logs[i][:2] == ".." {

				if steps == 0 {
					continue
				}

				steps -= 1
			} else {
				steps += 1
			}
		}
	}

	return steps
}

func main() {
	var logs []string
	var sol int

	logs = []string{"d1/", "d2/", "../", "d21/", "./"}
	sol = minOperations(logs)
	fmt.Println(sol)

	logs = []string{"d1/", "d2/", "./", "d3/", "../", "d31/"}
	sol = minOperations(logs)
	fmt.Println(sol)

	logs = []string{"d1/", "../", "../", "../"}
	sol = minOperations(logs)
	fmt.Println(sol)
}
