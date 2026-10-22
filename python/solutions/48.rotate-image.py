#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        startPos = 0
        
        while startPos < n // 2:
            endPos = n - 1 - startPos
            for i in range(endPos - startPos):
                temp = matrix[startPos][startPos + i]
                matrix[startPos][startPos + i] = matrix[endPos - i][startPos]
                matrix[endPos - i][startPos] = matrix[endPos][endPos - i]
                matrix[endPos][endPos - i] = matrix[startPos + i][endPos]
                matrix[startPos + i][endPos] = temp
            
            startPos += 1
        return
            # @lc code=end
