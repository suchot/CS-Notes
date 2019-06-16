# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.count = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '$'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' +self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        self.count += 1  #　要在下面用self.Deserialize　前先加。所以不能放后面.

        l = s.split(',')
#        if self.count > len(l):    #这句没用
#            return None
        if l[self.count] != '$':
            root = TreeNode(int(l[self.count]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        else:
            root = None
        return root
