#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split(' ')
        hTable1 = {}
        hTable2 = {}
        if len(pattern) != len(lst):
            return False
        for i in range(len(pattern)):
            if lst[i] in hTable1 and hTable1[lst[i]] != pattern[i]:
                return False
            if pattern[i] in hTable2 and hTable2[pattern[i]] != lst[i]:
                return False
            hTable1[lst[i]] = pattern[i]
            hTable2[pattern[i]] = lst[i]

        return True

# @lc code=end
