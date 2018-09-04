"""
Date: 2018/8/29
"""


class Solution:
    def reOrderArray(self, array):
        odd = []
        even = []
        for x in array:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)
        odd.extend(even)
        return odd