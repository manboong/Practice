#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_line = []
        cur_len = 0  # 현재 줄에 들어간 단어들의 순수 길이 합

        for word in words:
            # cur_len + len(word) : 단어들의 순수 길이 합
            # len(cur_line) : 단어 사이에 들어가야 할 최소 1개의 공백 개수 (새 단어 포함)
            if cur_len + len(word) + len(cur_line) > maxWidth:
                # 1. 현재 줄이 가득 차서 정렬 후 res에 추가
                total_spaces = maxWidth - cur_len

                if len(cur_line) == 1:
                    # 단어가 1개인 경우: 왼쪽 정렬 후 오른쪽에 공백 채움
                    res.append(cur_line[0] + " " * total_spaces)
                else:
                    # 단어가 여러 개인 경우: 공백 균등 배분
                    gaps = len(cur_line) - 1
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps

                    line_str = ""
                    for i in range(gaps):
                        line_str += cur_line[i]
                        # 기본 공백 + 나머지가 남아있으면 1개 추가
                        spaces_to_add = space_per_gap + \
                            (1 if i < extra_spaces else 0)
                        line_str += " " * spaces_to_add
                    line_str += cur_line[-1]
                    res.append(line_str)

                # 다음 줄을 위해 초기화
                cur_line = []
                cur_len = 0

            cur_line.append(word)
            cur_len += len(word)

        # 2. 마지막 줄 처리 (왼쪽 정렬, 단어 사이 1개 공백, 오른쪽에 남은 공백 채움)
        last_line_str = " ".join(cur_line)
        last_line_str += " " * (maxWidth - len(last_line_str))
        res.append(last_line_str)

        return res

# @lc code=end
