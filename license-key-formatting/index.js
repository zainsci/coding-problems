/**
 * source: https://leetcode.com/problems/license-key-formatting/
 * problem: https://leetcode.com/problems/license-key-formatting/
 * type: Easy
 * site: LeetCode
 */

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var licenseKeyFormatting = function (s, k) {
	s = s.replace(/-/gi, "").toUpperCase()
	let o = ""
	let sLen = s.length

	while (sLen > 0) {
		if ((s.length - sLen) % k === 0) {
			if (s.length === sLen) o = s[sLen - 1] + o
			else o = s[sLen - 1] + "-" + o
		} else {
			o = s[sLen - 1] + o
		}

		--sLen
	}

	return o
}

console.log(licenseKeyFormatting("5F3Z-2e-9-w", 4))
console.log(licenseKeyFormatting("2-5g-3-J", 2))
