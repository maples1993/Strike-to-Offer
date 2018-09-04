"""
Date: 2018/9/3
***
"""


class Solution:
    def multiply(self, A):
        # write code here
        if len(A) < 2:
            return []

        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]

        val = 1
        for i in range(len(A) - 2, -1, -1):
            val *= A[i + 1]
            B[i] *= val
        return B