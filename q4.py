"""
Date: 2018/8/29
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None

        root = TreeNode(pre.pop(0))
        pivot = 0
        while tin[pivot] != root.val:
            pivot += 1
        root.left = self.reConstructBinaryTree(pre, tin[0:pivot])
        root.right = self.reConstructBinaryTree(pre, tin[pivot+1:])
        return root

