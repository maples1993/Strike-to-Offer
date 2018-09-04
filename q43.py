"""
Date: 2018/9/1
YX = (X^T Y^T)^T
"""


class Solution:
    def process(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def LeftRotateString(self, s, n):
        # write code here
        if len(s) < 2:
            return s

        n = n % len(s)
        s = list(s)

        self.process(s, 0, n-1)
        self.process(s, n, len(s)-1)
        self.process(s, 0, len(s)-1)

        return ''.join(s)
