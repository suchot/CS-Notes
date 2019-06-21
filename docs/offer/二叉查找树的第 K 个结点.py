# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    # 利用二叉查找树中序遍历有序的特点。
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k == 0:
            return None
        res = list()
        def Traversal(node):
            if len(res) >= k or not node:
                return None
            Traversal(node.left)
            res.append(node)
            Traversal(node.right)
        Traversal(pRoot)
        if len(res) < k:
            return None
        return res[k-1]
