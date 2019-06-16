# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, target):
        # write your code here
        if not root:
            return []
        paths = []
        def dfs(root, sum, path, paths):
            if not root.left and not root.right and root.val == sum:
                path.append(root.val)
                paths.append(path)
            if root.left:
                dfs(root.left, sum-root.val, path+[root.val], paths) # 为什么上面用append就可以 这里就要path + []
            if root.right:
                dfs(root.right, sum-root.val, path+[root.val], paths)
                
        dfs(root, target, [], paths)
        return paths

