"""
Date: 2018/8/29
***
"""


class Solution:
    def process(self, matrix, start):
        res = []
        rows = len(matrix)
        cols = len(matrix[0])

        end_x = cols - start - 1
        end_y = rows - start - 1

        for i in range(start, end_x + 1):
            res.append(matrix[start][i])

        for i in range(start + 1, end_y+1):
            res.append(matrix[i][end_x])

        if end_y > start:
            for i in range(end_x - 1, start - 1, -1):
                res.append(matrix[end_y][i])

        if end_x > start:
            for i in range(end_y - 1, start, -1):
                res.append(matrix[i][start])

        return res

    def printMatrix(self, matrix):
        if not matrix:
            return []

        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        while start * 2 < rows and start * 2 < cols:
            res.extend(self.process(matrix, start))
            start += 1
        return res
