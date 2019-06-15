# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        dummy = ListNode(0)
        dummy.next = pHead
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val: 
                temp = cur.next.val 
                while cur.next and cur.next.val == temp:
                    cur.next = cur.next.next 
            else:
                cur = cur.next
        return dummy.next
            
