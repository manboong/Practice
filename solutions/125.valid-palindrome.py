#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = "".join(c for c in s if c.isalnum()).lower()
        for i in range(len(processed)):
            if processed[i] != processed[-i-1]:
                return False
        return True

# @lc code=end
