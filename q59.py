"""
Date: 2018/9/3
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        stack = [pRoot]
        width = 1
        to_right = True
        res = []
        while stack:
            layer = []
            for i in range(width):
                node = stack.pop(0)
                layer.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            width = len(stack)
            if to_right:
                res.append([x for x in layer])
            else:
                res.append([x for x in layer[::-1]])
            to_right = not to_right
        return res