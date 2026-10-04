#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rs = []
        for i in reversed(words):
            rs.append(i)
        return " ".join(rs)
# @lc code=end
