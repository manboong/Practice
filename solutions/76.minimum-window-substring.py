#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # 1. t의 문자 빈도수 계산 (Counter 대신 dict 사용)
        target_counts = {}
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1

        window_counts = {}
        need = len(target_counts)
        have = 0

        res_len = float("inf")
        res_bounds = (-1, -1)

        left = 0
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # 현재 문자가 목표 개수를 충족했는지 확인
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # 모든 조건이 충족되면 윈도우를 왼쪽에서 줄여가며 최소 길이 탐색
            while have == need:
                if (right - left + 1) < res_len:
                    res_len = right - left + 1
                    res_bounds = (left, right)

                left_char = s[left]
                window_counts[left_char] -= 1

                # 빈도수가 요구치 미만으로 떨어지면 have 감소
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1

                left += 1

        l, r = res_bounds
        return s[l: r + 1] if res_len != float("inf") else ""


# @lc code=end
