# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        p = [pRoot]
        res = []
        floor = 1
        while p:
            size = len(p)
            each_row = []
            for i in p:
                each_row.append(i.val)
            if floor&1 != 1:
                each_row.reverse()
            res.append(each_row)
            for i in range(size):
                tem = p.pop(0)
                if tem.left:
                    p.append(tem.left)
                if tem.right:
                    p.append(tem.right)
            floor += 1
        return res

