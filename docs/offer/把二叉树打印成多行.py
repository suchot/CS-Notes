# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        p = [pRoot]
        while p:
            size = len(p)
            each_row = []
            for i in p:
                each_row.append(i.val)
            res.append(each_row)
            for i in range(size):
                t = p.pop(0)
                if t.left:
                    p.append(t.left)
                if t.right:
                    p.append(t.right)
        return res
