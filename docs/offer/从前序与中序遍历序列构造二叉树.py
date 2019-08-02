# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        root = TreeNode(root_val)
        
        inorder_left = inorder[:root_idx]
        inorder_right= inorder[root_idx+1:]
        
        preorder_left = preorder[1:root_idx+1]
        preorder_right =preorder[root_idx+1:]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root
if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    S = Solution()
    print(S.buildTree(preorder, inorder))