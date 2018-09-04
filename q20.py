"""
Date: 2018/8/29
"""


class Solution:
    def __init__(self):
        self.elements = []
        self.min_val = []

    def push(self, node):
        # write code here
        self.elements.append(node)

        if not self.min_val or node < self.min_val[-1]:
            self.min_val.append(node)
        else:
            self.min_val.append(self.min_val[-1])

    def pop(self):
        # write code here
        if not self.elements:
            return None
        else:
            self.min_val.pop(-1)
            return self.elements.pop(-1)

    def top(self):
        # write code here
        return self.elements[-1]

    def min(self):
        # write code here
        return self.min_val[-1]