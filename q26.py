"""
Date: 2018/8/31
***
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def process(self, root):
        if not root.left and not root.right:
            head = tail = root
            return head, tail

        head = tail = None
        if root.left:
            head_l, tail_l = self.process(root.left)
            tail_l.right = root
            root.left = tail_l
            head = head_l
            tail = root
        if root.right:
            head_r, tail_r = self.process(root.right)
            head_r.left = root
            root.right = head_r
            if not head:
                head = root
            tail = tail_r
        return head, tail

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None

        head, tail = self.process(pRootOfTree)
        return head
