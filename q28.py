"""
Date: 2018/8/31
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0

        num_dict = {}
        for x in numbers:
            if x not in num_dict:
                num_dict[x] = 1
            else:
                num_dict[x] += 1
            if num_dict[x] > len(numbers) / 2:
                return x

        return 0