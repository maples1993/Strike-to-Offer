"""
Date: 2018/8/31
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0

        max_sum = array[0]
        cur_sum = array[0]
        for x in array[1:]:
            cur_sum = max(cur_sum + x, x)
            max_sum = max(max_sum, cur_sum)
        return max_sum