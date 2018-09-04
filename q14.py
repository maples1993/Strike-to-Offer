"""
Date: 2018/8/29
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        length = 0
        p = head
        while p:
            length += 1
            p = p.next

        if k <= length:
            p = head
            for i in range(length - k):
                p = p.next
            return p
        else:
            return None
