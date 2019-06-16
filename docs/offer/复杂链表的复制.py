# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
import copy
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        dummy = pHead
        # 第一步
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext
        dummy = pHead
        # 第二步　复制随机节点
        while dummy:
            dummyrandom = dummy.random
            copynode= dummy.next
            if dummy.random:
                copynode.random = dummyrandom.next
            dummy = copynode.next
        # 第三步 把链表拆分为两个
        cur = pHead
        pCloneHead = pHead.next
        while cur.next:
            next = cur.next
            cur.next = next.next
            cur = next
        return pCloneHead
    

                
