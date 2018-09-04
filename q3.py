"""
Date: 2018/8/29
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []

        head = ListNode('#')
        while listNode:
            tmp = listNode
            listNode = listNode.next
            tmp.next = head.next
            head.next = tmp

        res = []
        head = head.next
        while head:
            res.append(head.val)
            head = head.next
        return res
