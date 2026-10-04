#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        l = len(s)
        n = len(words[0])
        m = len(words)

        d = dict()
        res = []

        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

        for i in range(n):
            left = i
            right = i
            crnt_cnt = dict()
            count = 0

            while right+n <= l:
                w = s[right:right+n]
                right += n

                if w in d:
                    if w in crnt_cnt:
                        crnt_cnt[w] += 1
                    else:
                        crnt_cnt[w] = 1
                    count += 1
                    while crnt_cnt[w] > d[w]:
                        left_w = s[left:left+n]
                        crnt_cnt[left_w] -= 1
                        count -= 1
                        left += n

                    if count == m:
                        res.append(left)
                else:
                    crnt_cnt.clear()
                    count = 0
                    left = right

        return res


# @lc code=end
