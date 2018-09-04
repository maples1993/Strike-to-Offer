"""
Date: 2018/9/1
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum == 0:
            return []

        res = []
        head = tail = 1
        cur_sum = 0
        while head <= tsum // 2:
            if cur_sum + tail < tsum:
                cur_sum += tail
                tail += 1
            elif cur_sum + tail > tsum:
                cur_sum -= head
                head += 1
            else:
                cur_sum += tail
                tail += 1
                res.append([j for j in range(head, tail)])
        return res
