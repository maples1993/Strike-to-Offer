"""
Date: 2018/8/29
"""


class Solution:
    def Power(self, base, exponent):
        minus = False
        if exponent < 0:
            exponent *= -1
            minus = True

        res = 1
        cur = base
        while exponent:
            if exponent & 1 == 1:
                res *= cur
            cur *= cur
            exponent >>= 1

        if minus:
            return 1 / res
        else:
            return res