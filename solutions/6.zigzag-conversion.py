#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        for i in range(numRows*2-2):
            try:
                for j in range(len(s)//(numRows-1)):
                    res += s[j*(numRows*2-2)]
            except IndexError:
                continue
        return res
# @lc code=end
