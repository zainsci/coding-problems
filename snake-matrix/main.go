package main

/**
 * source: https://leetcode.com/problems/snake-in-matrix/
 * problem: https://leetcode.com/problems/snake-in-matrix/
 * type: Easy
 * site: LeetCode
 * submission: https://leetcode.com/problems/snake-in-matrix/submissions/1639380993/
 */

func finalPositionOfSnake(n int, commands []string) int {
	pos := 0

	for _, cmd := range commands {
		switch cmd {
		case "UP":
			pos = pos - n
		case "DOWN":
			pos = pos + n
		case "LEFT":
			pos = pos - 1
		case "RIGHT":
			pos = pos + 1
		}
	}
	return pos
}

func main() {
	n := 2
	commands := []string{"RIGHT", "DOWN"}
	println(finalPositionOfSnake(n, commands))

	n = 3
	commands = []string{"DOWN", "RIGHT", "UP"}
	println(finalPositionOfSnake(n, commands))
}
