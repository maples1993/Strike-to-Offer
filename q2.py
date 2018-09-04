"""
Date: 2018/8/29
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        if not s:
            return ""

        res = ''
        for x in s:
            if x == ' ':
                res += '%20'
            else:
                res += x
        return res