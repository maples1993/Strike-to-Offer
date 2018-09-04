"""
Date: 2018/9/1
"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0

        left = 0
        right = len(data) - 1
        while left < right:
            mid = (left + right) // 2
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            else:
                left = mid
                break

        if data[left] != k:
            return 0
        else:
            i1 = left - 1
            i2 = left + 1
            count = 1
            while i1 >= 0 and data[i1] == k:
                i1 -= 1
                count += 1
            while i2 < len(data) and data[i2] == k:
                i2 += 1
                count += 1
            return count
