package main

import (
	"fmt"
	"strings"
)

/**
 * source: https://leetcode.com/problems/license-key-formatting/
 * problem: https://leetcode.com/problems/license-key-formatting/
 * type: Easy
 * site: LeetCode
 */

func licenseKeyFormatting(s string, k int) string {
	n := strings.ReplaceAll(strings.ToUpper(s), "-", "")
	out := ""

	for i := len(n); i > 0; i-- {
		if (len(n)-i)%k == 0 {
			if len(n) == i {
				out = string(n[i-1]) + out
			} else {
				out = string(n[i-1]) + "-" + out
			}
		} else {
			out = string(n[i-1]) + out
		}

	}

	return out
}

func main() {
	fmt.Println(licenseKeyFormatting("5F3Z-2e-9-w", 4))
	fmt.Println(licenseKeyFormatting("2-5g-3-J", 2))
}
