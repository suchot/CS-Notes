# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return None
        if  root.left or  root.right:
            self.swap(root)
            self.Mirror(root.left)
            self.Mirror(root.right)
    def swap(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp