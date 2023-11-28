"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
"""
class Solution():
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # initialize 9 hash sets for row checking, 9 for column checking, 9 for box checking
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # iterate through the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    box_index = (i // 3) * 3 + j // 3
                    if num in rows[i] or num in columns[j] or num in boxes[box_index]:
                        return False
                    rows[i].add(num)
                    columns[j].add(num)
                    boxes[box_index].add(num)
        
        return True