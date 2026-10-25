#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue

                        r, c = row + i, col + j

                        if 0 <= r < m and 0 <= c < n:
                            count += board[r][c] % 2

                match board[row][col]:
                    case 0:
                        if count == 3:
                            board[row][col] = 2
                    case 1:
                        if count < 2:
                            board[row][col] = 3
                        elif count == 2 or count == 3:
                            board[row][col] = 1
                        elif count > 3:
                            board[row][col] = 3

        for row in range(m):
            for col in range(n):
                match board[row][col]:
                    case 2:
                        board[row][col] = 1
                    case 3:
                        board[row][col] = 0

# @lc code=end
