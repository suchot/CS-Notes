# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        #要注意k<=0的情况
        if not head or k<=0:
            return None
        
        phead = head
        head_k = head
        #这里只走k-1步
        while k>1:
            if not head_k.next:
                return None
            head_k = head_k.next
            k -= 1
        while head_k.next:
            head_k = head_k.next
            phead = phead.next
        return phead