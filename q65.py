"""
Date: 2018/9/4
"""


class Solution:
    def process(self, matrix, flag, x, y, path):
        if not path:
            return True

        if 0 <= x < len(matrix[0]) and 0 <= y < len(matrix):
            if flag[y][x] == 0 and matrix[y][x] == path[0]:
                flag[y][x] = 1
                if self.process(matrix, flag, x+1, y, path[1:]) \
                        or self.process(matrix, flag, x-1, y, path[1:]) \
                        or self.process(matrix, flag, x, y+1, path[1:]) \
                        or self.process(matrix, flag, x, y-1, path[1:]):
                    return True
                else:
                    flag[y][x] = 0
        return False

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False

        mat = []
        flag = []
        for i in range(rows):
            mat.append([matrix[i * cols + j] for j in range(cols)])
            flag.append([0] * cols)

        for x in range(cols):
            for y in range(rows):
                if self.process(mat, flag, x, y, path):
                    return True
        return False
