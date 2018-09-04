"""
Date: 2018/8/31
"""


class Solution:
    def partition(self, tinput, left, right):
        mid = (left + right) // 2

        pivot = tinput[mid]
        bound = left
        tinput[mid], tinput[right] = tinput[right], tinput[mid]
        for i in range(left, right):
            if tinput[i] < pivot:
                tinput[bound], tinput[i] = tinput[i], tinput[bound]
                bound += 1
        tinput[bound], tinput[right] = tinput[right], tinput[bound]
        return bound

    def process(self, tinput, left, right, k):
        if left < right:
            pivot = self.partition(tinput, left, right)
            if pivot == k - 1:
                return
            self.process(tinput, pivot + 1, right, k)
            self.process(tinput, left, pivot - 1, k)

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k == 0 or k > len(tinput):
            return None

        self.process(tinput, 0, len(tinput) - 1, k)

        return tinput


if __name__ == '__main__':
    tinput = [4,5,1,6,2,7,3,8]

    s = Solution()
    print(s.GetLeastNumbers_Solution(tinput, 8))
