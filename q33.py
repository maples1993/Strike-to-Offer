"""
Date: 2018/9/1
***
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return None

        res = [1]
        p2 = p3 = p5 = 0
        while len(res) < index:
            item = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
            if item == res[p2] * 2:
                p2 += 1
            if item == res[p3] * 3:
                p3 += 1
            if item == res[p5] * 5:
                p5 += 1
            res.append(item)
        return res[-1]


s = Solution()
print(s.GetUglyNumber_Solution(7))
