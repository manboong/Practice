#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n=len(words[0])
        wordSet=set(words)

        for i in range(len(s)):
            tempSet=wordSet
            tempWord=""
            for j in range(n):
                tempWord+=s[j]
            if not tempWord in wordSet:
                continue
            else:
                tempSet.remove(tempWord)
                while tempSet:





# @lc code=end

