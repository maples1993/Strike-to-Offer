"""
Date: 2018/9/4
***
"""


class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def max_heap_insert(self, num):
        self.maxHeap.append(num)
        i = len(self.maxHeap) - 1
        while i > 0:
            if self.maxHeap[i] > self.maxHeap[(i - 1) // 2]:    # 父节点比较
                self.maxHeap[i], self.maxHeap[(i - 1) // 2] = self.maxHeap[(i - 1) // 2], self.maxHeap[i]
                i = (i - 1) // 2
            else:
                break

    def max_heap_pop(self):
        top = self.maxHeap[0]
        self.maxHeap[0] = self.maxHeap[-1]
        self.maxHeap.pop(-1)

        i = 0
        while 2 * i + 1 < len(self.maxHeap):
            next_i = 2 * i + 1
            if next_i + 1 < len(self.maxHeap) and self.maxHeap[next_i + 1] > self.maxHeap[next_i]:
                next_i += 1
            if self.maxHeap[i] < self.maxHeap[next_i]:
                self.maxHeap[i], self.maxHeap[next_i] = self.maxHeap[next_i], self.maxHeap[i]
            else:
                break
        return top

    def min_heap_insert(self, num):
        self.minHeap.append(num)
        i = len(self.minHeap) - 1
        while i > 0:
            if self.minHeap[i] < self.minHeap[(i - 1) // 2]:
                self.minHeap[i], self.minHeap[(i - 1) // 2] = self.minHeap[(i - 1) // 2], self.minHeap[i]
                i = (i - 1) // 2
            else:
                break

    def min_heap_pop(self):
        top = self.minHeap[0]
        self.minHeap[0] = self.minHeap[-1]
        self.minHeap.pop(-1)

        i = 0
        while 2 * i + 1 < len(self.minHeap):
            next_i = 2 * i + 1
            if next_i + 1 < len(self.minHeap) and self.minHeap[next_i + 1] < self.minHeap[next_i]:
                next_i += 1
            if self.minHeap[i] > self.minHeap[next_i]:
                self.minHeap[i], self.minHeap[next_i] = self.minHeap[next_i], self.minHeap[i]
            else:
                break
        return top

    def Insert(self, num):
        # write code here
        if len(self.maxHeap) == len(self.minHeap):
            if len(self.minHeap) > 0 and num < self.maxHeap[0]:
                self.max_heap_insert(num)   # 插入后两堆大小不同
                num = self.max_heap_pop()
            self.min_heap_insert(num)   # 保证最小堆≥最大堆
        else:
            if len(self.minHeap) > 0 and num > self.minHeap[0]:
                self.min_heap_insert(num)
                num = self.min_heap_pop()
            self.max_heap_insert(num)

    def GetMedian(self, fuck=None):
        # write code here
        if len(self.maxHeap) + len(self.minHeap) == 0:
            return None

        if len(self.maxHeap) == len(self.minHeap):
            return (self.maxHeap[0] + self.minHeap[0]) / 2.
        else:
            return self.minHeap[0]