#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left = 0
        currentSum = 0
        minLength = len(nums)

        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum >= target:
                minLength = min(minLength, right-left+1)
                currentSum -= nums[left]
                left += 1

        return minLength



# @lc code=end
