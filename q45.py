"""
Date: 2018/9/1
"""


class Solution:
    def process(self, numbers):
        for i in range(1, len(numbers)):
            target = numbers[i]
            for j in range(i-1, -1, -1):
                if numbers[j] > target:
                    numbers[j + 1] = numbers[j]
                else:
                    j +=1
                    break
            numbers[j] = target

    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False

        self.process(numbers)
        zero_count = 0
        for i, x in enumerate(numbers):
            if x == 0:
                zero_count += 1
            else:
                break

        for j in range(i+1, len(numbers)):
            if numbers[j] == numbers[j - 1]:
                return False
            while numbers[j] != numbers[j-1] + 1:
                zero_count -= 1
                numbers[j-1] += 1
                if zero_count < 0:
                    return False
        return True