"""
Date: 2018/9/1
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def process(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        depth_l = self.process(root.left)
        depth_r = self.process(root.right)

        if depth_l == -1 or depth_r == -1 or abs(depth_l - depth_r) > 1:
            return -1

        return 1 + max(depth_l, depth_r)

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True

        depth = self.process(pRoot)
        if depth == -1:
            return False
        else:
            return True