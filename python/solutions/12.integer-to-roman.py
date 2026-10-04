#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []
        while num > 0:
            if num >= 1000:
                roman.append("M"*(num//1000))
                num %= 1000
            elif num >= 900:
                roman.append("C")
                roman.append("M")
                num %= 900
            elif num >= 500:
                roman.append("D")
                num %= 500
            elif num >= 400:
                roman.append("C")
                roman.append("D")
                num %= 400
            elif num >= 100:
                roman.append("C"*(num//100))
                num %= 100
            elif num >= 90:
                roman.append("X")
                roman.append("C")
                num %= 90
            elif num >= 50:
                roman.append("L")
                num %= 50
            elif num >= 40:
                roman.append("X")
                roman.append("L")
                num %= 40
            elif num >= 10:
                roman.append("X"*(num//10))
                num %= 10
            elif num == 9:
                roman.append("I")
                roman.append("X")
                num %= 9
            elif num >= 5:
                roman.append("V")
                num %= 5
            elif num == 4:
                roman.append("I")
                roman.append("V")
                num %= 4
            elif num >= 1:
                roman.append("I"*(num//1))
                num %= 1

        return "".join(roman)

# @lc code=end
