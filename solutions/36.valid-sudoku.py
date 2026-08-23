#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            currentTable = set()
            for val in row:
                if val == ".":
                    continue
                if val in currentTable:
                    return False
                currentTable.add(val)
                
        for colNum in range(9):
            currentTable = set()
            for rowNum in range(9):
                val = board[rowNum][colNum]
                if val == ".":
                    continue
                if val in currentTable:
                    return False
                currentTable.add(val)
                
        for blockRow in range(3):
            for blockCol in range(3):
                currentTable = set()
                for subRow in range(3):
                    for subCol in range(3):
                        val = board[3 * blockRow + subRow][3 * blockCol + subCol]
                        if val == ".":
                            continue
                        if val in currentTable:
                            return False
                        currentTable.add(val)
                        
        return True

# @lc code=end
