"""
Date: 2018/8/29
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        head = ListNode('#')
        while pHead:
            tmp = pHead
            pHead = pHead.next
            tmp.next = head.next
            head.next = tmp
        return head.next

