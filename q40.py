"""
Date: 2018/9/1
***
"""


class Solution:
    def is_1bit(self, num, index):
        num >>= index
        return num & 1

    def last_1bit(self, num):
        index = 0
        while num & 1 == 0 and index < 32 * 8:
            num >>= 1
            index += 1
        return index

    def FindNumsAppearOnce(self, array):
        # write code here
        xor = 0
        for x in array:
            xor ^= x

        index = self.last_1bit(xor)
        a = b = 0
        for x in array:
            if self.is_1bit(x, index):
                a ^= x
            else:
                b ^= x
        return [a, b]

