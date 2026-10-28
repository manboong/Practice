#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        indexS = [0] * 200  # Stores index of characters in string s
        indexT = [0] * 200  # Stores index of characters in string t

        length = len(s)  # Get the length of both strings

        # If the lengths of the two strings are different, they can't be isomorphic
        if length != len(t):
            return False

        for i in range(length):  # Iterate through each character of the strings
            # Check if the index of the current character in string s is different from the index of the corresponding character in string t
            if indexS[ord(s[i])] != indexT[ord(t[i])]:
                return False  # If different, strings are not isomorphic

            indexS[ord(s[i])] = i + 1  # updating position of current character
            indexT[ord(t[i])] = i + 1

        return True  # If the loop completes without returning false, strings are isomorphic

# @lc code=end
