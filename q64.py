"""
Date: 2018/9/4
***
"""


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        max_val = []
        window = []

        for i in range(len(num)):
            while window and num[window[-1]] <= num[i]:
                window.pop(-1)
            if window and i - window[0] + 1 > size:
                window.pop(0)
            window.append(i)
            if 0 < size <= i + 1:
                max_val.append(num[window[0]])
        return max_val