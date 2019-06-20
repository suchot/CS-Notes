# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l1,l2 = pHead1, pHead2
        while (l1 != l2):
            if l1:
                l1 = l1.next
            else:
                l1 = pHead2
            if l2:
                l2 = l2.next
            else:
                l2 = pHead1
        return l1 