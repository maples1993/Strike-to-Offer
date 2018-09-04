"""
Date: 2018/9/1
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None

        l1 = 0
        l2 = 0
        p1 = pHead1
        p2 = pHead2
        while p1:
            l1 += 1
            p1 = p1.next
        while p2:
            l2 += 1
            p2 = p2.next

        while l1 != l2:
            if l1 > l2:
                pHead1 = pHead1.next
                l1 -= 1
            else:
                pHead2 = pHead2.next
                l2 -= 1

        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return pHead1