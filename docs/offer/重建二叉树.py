# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            pin = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:pin+1], tin[:pin])
            root.right = self.reConstructBinaryTree(pre[pin+1:], tin[pin+1:])