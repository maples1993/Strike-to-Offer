"""
Date: 2018/8/29
"""


class Solution:
    def __init__(self):
        self.bottom = []
        self.top = []

    def push(self, node):
        # write code here
        self.bottom.append(node)

    def pop(self):
        if not self.top:
            while self.bottom:
                self.top.append(self.bottom.pop(-1))
        if self.top:
            return self.top.pop(-1)
        else:
            return None