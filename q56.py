"""
Date: 2018/9/3
***
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None

        new_head = ListNode('#')
        p1 = new_head
        p2 = pHead
        p2_pre = p2
        cur_val = pHead.val
        count = 0
        while p2:
            if p2.val == cur_val:
                count += 1
            else:
                cur_val = p2.val
                if count == 1:
                    p1.next = p2_pre
                    p1 = p1.next
                count = 1
                p2_pre = p2
            p2 = p2.next
        if count == 1:
            p1.next = p2_pre
            p1 = p1.next
        p1.next = None
        return new_head.next