"""
Date: 2018/9/1
***
"""


class Solution:
    def merge(self, data, buffer, left, mid, right):
        i1 = left
        i2 = mid + 1
        count = 0
        for i in range(left, right+1):
            if i1 > mid:
                buffer[i] = data[i2]
                i2 += 1
            elif i2 > right:
                buffer[i] = data[i1]
                i1 += 1
            elif data[i1] <= data[i2]:
                buffer[i] = data[i1]
                i1 += 1
            else:
                buffer[i] = data[i2]
                i2 += 1
                count += mid - i1 + 1   # mid两端是以排好序的
        data[left:right+1] = buffer[left:right+1]
        return count

    def process(self, data, buffer, left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += self.process(data, buffer, left, mid)
            count += self.process(data, buffer, mid + 1, right)
            count += self.merge(data, buffer, left, mid, right)
        return count

    def InversePairs(self, data):
        # write code here
        if len(data) < 2:
            return 0

        buffer = [0 for i in range(len(data))]
        count = self.process(data, buffer, 0, len(data) - 1)
        return count % 1000000007
