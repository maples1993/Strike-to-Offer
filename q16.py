"""
Date: 2018/8/29
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        head = ListNode('#')
        tail = head

        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                tail.next = pHead1
                pHead1 = pHead1.next
            else:
                tail.next = pHead2
                pHead2 = pHead2.next
            tail = tail.next

        if pHead1:
            tail.next = pHead1
        else:
            tail.next = pHead2

        return head.next

