"""
Date: 2018/9/1
***
"""


class Solution:
    def cmp(self, num1, num2):
        s1 = num1 + num2
        s2 = num2 + num1
        return s1 < s2

    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return None

        numbers = list(map(str, numbers))
        for i in range(1, len(numbers)):
            target = numbers[i]
            for j in range(i-1, -1, -1):
                if self.cmp(target, numbers[j]):
                    numbers[j + 1] = numbers[j]
                else:
                    j += 1
                    break
            numbers[j] = target
        return ''.join(numbers)
