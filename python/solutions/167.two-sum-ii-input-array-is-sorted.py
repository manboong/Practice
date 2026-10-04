#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        sum = numbers[left]+numbers[right]
        while left < right:
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            sum = numbers[left]+numbers[right]
            if sum == target:
                return [left+1, right+1]


# @lc code=end
