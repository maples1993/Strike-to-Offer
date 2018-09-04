"""
Date: 2018/8/29
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        res = [0, 1]

        for i in range(1, number):
            res.append(2 * res[-1])

        return res[number]