"""
Date: 2018/9/3
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None

        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
        else:
            while pNode.next and pNode.next.left != pNode:
                pNode = pNode.next
            pNode = pNode.next
        return pNode