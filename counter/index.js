#!/usr/bin/env node
/**
 * source: https://leetcode.com/problems/counter/
 * problem: https://leetcode.com/problems/counter/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/counter/solutions/6721417/ts/
 */

/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
	let count = n

	return function () {
		return count++
	}
}

const counter = createCounter(10)
counter() // 10
counter() // 11
counter() // 12
