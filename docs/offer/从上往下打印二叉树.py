# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return res
        q =[root]
        while q:
            t = q.pop(0)
            res.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return res

