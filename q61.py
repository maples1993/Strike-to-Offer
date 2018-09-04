"""
Date: 2018/9/4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        if not root:
            return ['#']
        else:
            return [root.val] + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        if not s:
            return None

        node = s.pop(0)
        if node != '#':
            root = TreeNode(node)
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        else:
            root = None
        return root
