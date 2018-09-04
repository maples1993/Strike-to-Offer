"""
Date: 2018/9/3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def process(self, p1, p2):
        if not p1 and not p2:
            return True

        if p1 and p2 and p1.val == p2.val:
            return self.process(p1.left, p2.right) \
                   and self.process(p1.right, p2.left)
        else:
            return False

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True

        return self.process(pRoot, pRoot)