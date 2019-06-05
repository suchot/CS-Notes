# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        else:
            while pNode.next:
                parent = pNode.next
                if parent.left == pNode:
                    return parent
                else:
                    pNode = parent
            return None
