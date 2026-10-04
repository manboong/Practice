#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        idx = 0

        while idx < len(s):
            for r in range(numRows):
                if idx < len(s):
                    rows[r].append(s[idx])
                    idx += 1
            for r in range(numRows - 2, 0, -1):
                if idx < len(s):
                    rows[r].append(s[idx])
                    idx += 1
        return "".join("".join(row) for row in rows)

# @lc code=end
