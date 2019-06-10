# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.symmetrical(pRoot.left, pRoot.right)
    def symmetrical(self, lroot, rroot):
        if not lroot and not rroot:
            return True
        if not rroot or not lroot:
            return False
        if lroot.val != rroot.val:
            return False
        return self.symmetrical(lroot.left, rroot.right) and self.symmetrical(lroot.right, rroot.left)
        