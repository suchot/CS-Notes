# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归版本

class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

# 将左子树构建成双链表，返回链表头
        left = self.Convert(pRootOfTree.left)
        p = left

        # 定位至左子树的最右的一个结点
        while p and p.right:
            p = p.right

        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            pRootOfTree.left = p
            p.right = pRootOfTree

        # 将右子树构造成双链表，返回链表头
        right = self.Convert(pRootOfTree.right)
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        # 如果右子树不为空，将该链表追加到root结点之后
        
        
        #很关键 最后返回得是最左侧得头节点
        if left:
            return left
        else:
            return pRootOfTree
