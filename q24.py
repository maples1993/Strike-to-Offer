"""
Date: 2018/8/31
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.trace = []
        self.res = []

    def sort(self):
        if self.res:
            for i in range(1, len(self.res)):
                target = self.res[i]
                for j in range(i - 1, -1, -1):
                    if len(self.res[j]) <= len(target):
                        self.res[j + 1] = self.res[j]
                    else:
                        j += 1
                        break
                self.res[j] = target

    def process(self, root, expectNumber):
        self.trace.append(root.val)

        if not root.left and not root.right:    # 叶子节点
            if expectNumber == root.val:
                self.res.append([x for x in self.trace])

        if root.left:
            self.process(root.left, expectNumber - root.val)
        if root.right:
            self.process(root.right, expectNumber - root.val)
        self.trace.pop(-1)

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.process(root, expectNumber)
        self.sort()
        return self.res
