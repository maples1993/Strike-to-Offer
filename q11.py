"""
Date: 2018/8/29
"""


class Solution:
    def NumberOf1(self, n):
        count = 0

        n &= 0xFFFFFFFF
        while n:
            n &= (n - 1)
            count += 1

        return count