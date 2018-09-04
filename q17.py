"""
Date: 2018/8/29
*****
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def process(self, root1, root2):
        if not root1 and root2:
            return False
        if not root2:
            return True
        if root1.val != root2.val:
            return False

        return self.process(root1.left, root2.left) \
               and self.process(root1.right, root2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False

        res = False
        if pRoot1.val == pRoot2.val:
            res = self.process(pRoot1, pRoot2)

        if not res:
            res = self.HasSubtree(pRoot1.left, pRoot2) \
                   or self.HasSubtree(pRoot1.right, pRoot2)
        return res
