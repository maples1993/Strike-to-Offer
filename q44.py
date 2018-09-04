"""
Date: 2018/9/1
"""


class Solution:
    def process(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def ReverseSentence(self, s):
        # write code here
        if len(s) < 2:
            return s

        s = list(s)
        left = -1
        right = -1
        flag = False
        for i, x in enumerate(s):
            if x != ' ':
                if not flag:
                    flag = True
                    left = right = i
                else:
                    right += 1
                    if i == len(s) - 1:     # 注意边界情况
                        self.process(s, left, right)
            else:
                if flag:
                    flag = False
                    self.process(s, left, right)
        self.process(s, 0, len(s) - 1)
        return ''.join(s)
