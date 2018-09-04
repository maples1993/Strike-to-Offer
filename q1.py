"""
Date: 2018/8/29
"""


class Solution:
    def Find(self, target, array):
        if not array:
            return False

        rows = len(array)
        cols = len(array[0])

        x = 0
        y = rows - 1
        while x < cols and y >= 0:
            if array[x][y] == target:
                return True
            elif array[x][y] > target:
                y -= 1
            else:
                x += 1
        return False