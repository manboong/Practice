#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_tank = 0
        current_tank = 0
        start_index = 0

        for i in range(len(gas)):
            current_tank += gas[i]-cost[i]
            if current_tank < 0:
                start_index = i+1
                current_tank = 0

        return start_index


# @lc code=end
