"""
Date: 2018/8/29
"""


class Solution:
    def rectCover(self, number):
        res = [0, 1, 2]

        for i in range(2, number):
            res.append(res[-1] + res[-2])

        return res[number]