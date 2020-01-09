
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, posorder, inorder):
        if not posorder:
            return None
        root_val = posorder[-1]
        root_idx = inorder.index(root_val)
        root = TreeNode(root_val)
        
        inorder_left = inorder[:root_idx]
        inorder_right= inorder[root_idx+1:]
        
        posorder_left = posorder[:root_idx]
        posorder_right =posorder[root_idx:-1]
        
        root.left = self.buildTree(posorder_left, inorder_left)
        root.right = self.buildTree(posorder_right, inorder_right)
        
        return root
    def preorder(self,root):
        if not root:
            return []
        res = []
        stack =[root]
        while stack:
            node  = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ''.join(res)
if __name__ == "__main__":
    inorder = list(input().strip())

    posorder = list(input().strip())
    S = Solution()
    root = S.buildTree(posorder, inorder)
    print(S.preorder(root))