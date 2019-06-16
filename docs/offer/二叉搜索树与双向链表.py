# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)
        p = left
        while p and p.right:
            p = p.right
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p
        right = self.Convert(pRootOfTree.right)
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right
        if left:
            return left
        else:
            return pRootOfTree
