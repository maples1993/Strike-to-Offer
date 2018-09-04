"""
Date: 2018/9/3
"""


class Solution:
    def __init__(self):
        self.count = 0
        self.log = {}

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        min_val = self.count + 1
        c = '#'
        for key in self.log:
            if self.log[key] != -1 and self.log[key] < min_val:
                min_val = self.log[key]
                c = key
        return c

    def Insert(self, char):
        # write code here
        self.count += 1
        if char not in self.log:
            self.log[char] = self.count
        else:
            self.log[char] = -1