"""
Date: 2018/9/3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None

        p1 = pHead
        p2 = pHead.next
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next.next

        if p1 and p2:
            length = 1
            p2 = p2.next
            while p2 != p1:
                p2 = p2.next
                length += 1

            p1 = p2 = pHead
            for i in range(length):
                p2 = p2.next
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
        else:
            return None
