"""
Date: 2018/9/4
"""


class Solution:
    def __init__(self):
        self.count = 0

    def process(self, flag, x, y, threshold):
        if 0 <= x < len(flag[0]) and 0 <= y < len(flag):
            if flag[y][x] == 0:
                bit_sum = 0
                num = x
                while num:
                    bit_sum += num % 10
                    num //= 10
                num = y
                while num:
                    bit_sum += num % 10
                    num //= 10
                if bit_sum <= threshold:
                    flag[y][x] = 1
                    self.count += 1

                    self.process(flag, x + 1, y, threshold)
                    self.process(flag, x - 1, y, threshold)
                    self.process(flag, x, y + 1, threshold)
                    self.process(flag, x, y - 1, threshold)

    def movingCount(self, threshold, rows, cols):
        # write code here
        flag = []
        for i in range(rows):
            flag.append([0] * cols)

        self.process(flag, 0, 0, threshold)
        return self.count