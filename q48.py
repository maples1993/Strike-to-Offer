"""
Date: 2018/9/1
***
"""


class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            num1, num2 = num1 ^ num2, (num1 & num2) << 1
            num1 &= 0xFFFFFFFF  # 和
            num2 &= 0xFFFFFFFF  # 进位
            if num1 > 0x7FFFFFFF:   # 符号位为1
                num1 = ~(num1 ^ 0xFFFFFFFF)
        return num1
