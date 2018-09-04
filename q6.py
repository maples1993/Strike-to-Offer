"""
Date: 2018/8/29
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        left = 0
        right = len(rotateArray) - 1
        while left < right:
            mid = (left + right) // 2
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            else:
                right = mid
        return rotateArray[left]