#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res = [1]*n
        for i in range(1, n):
            if ratings[i-1] > ratings[i]:
                res[i-1] = res[i]+1
            if ratings[i-1] < ratings[i]:
                res[i] = res[i-1]+1

        for i in reversed(range(n-1)):
            if ratings[i+1] > ratings[i] and res[i+1] <= res[i]:
                res[i+1] = res[i]+1
            if ratings[i+1] < ratings[i] and res[i+1] >= res[i]:
                res[i] = res[i+1]+1
        return sum(res)


# @lc code=end
