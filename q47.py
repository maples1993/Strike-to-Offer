"""
Date: 2018/9/1
"""


class Solution:
    def __init__(self):
        self.res = 0

    def process(self, n):
        self.res += n
        return n > 1 and self.process(n-1)

    def Sum_Solution(self, n):
        # write code here
        self.process(n)
        return self.res