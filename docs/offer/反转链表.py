# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList1(self, pHead):
        # write code here
        #递归法
        if not pHead or not pHead.next:
            return pHead
        nHead = pHead.next
        pHead.next = None
        newHead = self.ReverseList(nHead)
        nHead.next = pHead
        return newHead
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        dummy = None
        while pHead:
            nHead = pHead.next
            pHead.next = dummy
            dummy = pHead
            pHead = nHead
        return dummy
            
