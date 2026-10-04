#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortedNums = sorted(nums)
        if sortedNums[0] == 0 and sortedNums[-1] == 0:
            return [[0, 0, 0]] if len(nums) >= 3 else []
        res = set()
        for m in range(1, len(nums)-1):
            l = 0
            r = len(nums)-1

            while l < m and m < r:
                if sortedNums[l]+sortedNums[m]+sortedNums[r] == 0:
                    sum = tuple(
                        sorted([sortedNums[l], sortedNums[m], sortedNums[r]]))

                    if not sum in res:
                        res.add(sum)

                    if m-l > m-r:
                        l += 1
                    else:
                        r -= 1

                elif sortedNums[l]+sortedNums[m]+sortedNums[r] < 0:
                    l += 1
                elif sortedNums[l]+sortedNums[m]+sortedNums[r] > 0:
                    r -= 1

        return list(res)
# @lc code=end
