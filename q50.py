"""
Date: 2018/9/1
"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        num_dict = {}
        for i in range(len(numbers)):
            num_dict[i] = 0

        for x in numbers:
            num_dict[x] += 1
            if num_dict[x] > 1:
                duplication[0] = x
                return True
        return False