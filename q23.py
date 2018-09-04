"""
Date: 2018/8/31
***
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        pivot = 0
        for i in range(len(sequence) - 1):
            if sequence[i] < sequence[-1]:
                pivot += 1
            else:
                break
        for i in range(pivot, len(sequence) - 1):
            if sequence[i] <= sequence[-1]:
                return False

        if pivot > 0 and not self.VerifySquenceOfBST(sequence[:pivot]):
            return False
        if pivot < len(sequence) - 1 and not self.VerifySquenceOfBST(sequence[pivot:-1]):
            return False

        return True