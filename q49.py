"""
Date: 2018/9/1
"""


class Solution:
    def StrToInt(self, s):
        # write code here
        res = 0

        bits = 0
        for i in range(len(s)-1, -1, -1):
            if ord('0') <= ord(s[i]) <= ord('9'):
                res += int(s[i]) * 10 ** bits
            elif i != 0:
                res = 0
                break
            bits += 1
        if len(s) > 0 and s[0] == '-':
            res *= -1
        return res
