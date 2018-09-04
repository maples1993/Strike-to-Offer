"""
Date: 2018/8/29
"""


class Solution:
    def Fibonacci(self, n):
        res = [0, 1]

        for i in range(1, n):
            res.append(res[-1] + res[-2])

        return res[n]