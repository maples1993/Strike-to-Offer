"""
Date: 2018/9/1
"""


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []

        num_dict = {}
        for x in array:
            num_dict[x] = tsum - x

        for x in num_dict:
            if num_dict[x] in num_dict:
                return [x, tsum - x]

        return []