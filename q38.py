"""
Date: 2018/9/1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        if not pRoot.left and not pRoot.right:
            return 1

        depth = 1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))
        return depth