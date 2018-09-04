"""
Date: 2018/9/4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k < 0:
            return None

        node = None
        if pRoot.left:
            node = self.KthNode(pRoot.left, k)
        if not node and self.count == k - 1:
            return pRoot
        self.count += 1
        if not node and pRoot.right:
            node = self.KthNode(pRoot.right, k)
        return node
