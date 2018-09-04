"""
Date: 2018/8/31
***
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, head):
        if not head:
            return None

        # step1: copy node
        p = head
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = node.next

        # step2: copy random
        p = head
        while p:
            node = p.random
            if node:
                p.next.random = node.next
            p = p.next.next

        # step3: split list
        new_head = head.next
        p1 = head
        p2 = new_head
        while p2.next:
            p1.next = p2.next
            p2.next = p1.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = None

        return new_head
