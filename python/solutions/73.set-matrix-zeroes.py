#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        isFirstColZero = False

        for row in range(m):
            if matrix[row][0] == 0:
                isFirstColZero = True

            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in reversed(range(m)):
            for col in reversed(range(1, n)):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

            if isFirstColZero:
                matrix[row][0] = 0


# @lc code=end
