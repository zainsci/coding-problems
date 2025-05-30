#!/usr/bin/env python3

"""
source: https://leetcode.com/problems/valid-sudoku/
problem: https://leetcode.com/problems/valid-sudoku/
type: Medium
site: LeetCode
submission: https://leetcode.com/problems/valid-sudoku/submissions/1648773712/
"""


class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isValidSudoku(self, board):

        # check rows & cols
        for x in range(len(board)):
            row = board[x]
            row_set = set()

            for elem in row:
                if elem == ".":
                    continue
                if elem in row_set:
                    return False
                row_set.add(elem)

            col_set = set()

            for y in range(len(row)):
                if board[y][x] == ".":
                    continue
                if board[y][x] in col_set:
                    return False
                col_set.add(board[y][x])

        # check each box
        col = 0
        for i in range(9):
            x = i % 3

            x1, x2, x3 = board[(x*3)][(col*3):(col*3)+3]
            y1, y2, y3 = board[(x*3)+1][(col*3):(col*3)+3]
            z1, z2, z3 = board[(x*3)+2][(col*3):(col*3)+3]
            col += 1 if (x*3)+2 == 8 else 0

            # print("---------")
            # print("|", x1, x2, x3, "|")
            # print("|", y1, y2, y3, "|")
            # print("|", z1, z2, z3, "|")
            # print("---------")

            box = [x1, x2, x3, y1, y2, y3, z1, z2, z3]
            box_set = set()
            for num in box:
                if num == ".":
                    continue
                if num in box_set:
                    return False
                box_set.add(num)

        return True


def main():
    sol = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(sol.isValidSudoku(board))

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(sol.isValidSudoku(board))

    pass


if __name__ == "__main__":
    main()
