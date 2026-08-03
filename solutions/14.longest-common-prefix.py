#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]

# @lc code=end
